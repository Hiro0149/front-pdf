/* ===== Front PDF 利用登録（アプリと公式ページで共通） =====
 * ・ID はアプリがブラウザごとに作るランダムな 8 文字。PC や個人の情報は一切使わない。
 * ・公式ページは ID から「登録テキスト」と 10 文字の「短縮コード」を発行する（計算はブラウザ内だけ。送信しない）。
 * ・アプリは同じ計算をして照合する。通信はしない。
 * ・目的は「公式ページを一度見てもらう」ことであり、強固なコピー防止ではない（オープンソースなので仕組みは公開）。
 */
var KoboLic=(function(){
  var SECRET='/*__LICSECRET__*/', VER='v1';
  var AL='23456789ABCDEFGHJKMNPQRSTUVWXYZ'; // 紛らわしい 0 O 1 I L を除いた 31 文字
  function sha256(str){ // 小さな SHA-256（UTF-8 文字列 → 32 バイト配列）
    var b=unescape(encodeURIComponent(str)),i,j,K=[],H=[],w=new Array(64),p=2,n=0;
    function isP(x){for(var f=2;f*f<=x;f++)if(x%f===0)return false;return true;}
    while(n<64){if(isP(p)){var r=Math.pow(p,1/3),s=Math.sqrt(p);if(n<8)H[n]=(s-Math.floor(s))*4294967296|0;K[n]=(r-Math.floor(r))*4294967296|0;n++;}p++;}
    var bytes=[];for(i=0;i<b.length;i++)bytes.push(b.charCodeAt(i));
    var bl=bytes.length*8;bytes.push(0x80);while(bytes.length%64!==56)bytes.push(0);
    for(i=7;i>=0;i--)bytes.push(i>3?0:(bl>>>(i*8))&255);
    for(i=0;i<bytes.length;i+=64){
      for(j=0;j<16;j++)w[j]=(bytes[i+j*4]<<24)|(bytes[i+j*4+1]<<16)|(bytes[i+j*4+2]<<8)|bytes[i+j*4+3];
      for(j=16;j<64;j++){var a=w[j-15],c=w[j-2];
        var s0=((a>>>7)|(a<<25))^((a>>>18)|(a<<14))^(a>>>3),s1=((c>>>17)|(c<<15))^((c>>>19)|(c<<13))^(c>>>10);
        w[j]=(w[j-16]+s0+w[j-7]+s1)|0;}
      var A=H[0],B=H[1],C=H[2],D=H[3],E=H[4],F=H[5],G=H[6],Hh=H[7];
      for(j=0;j<64;j++){
        var S1=((E>>>6)|(E<<26))^((E>>>11)|(E<<21))^((E>>>25)|(E<<7)),ch=(E&F)^(~E&G),t1=(Hh+S1+ch+K[j]+w[j])|0;
        var S0=((A>>>2)|(A<<30))^((A>>>13)|(A<<19))^((A>>>22)|(A<<10)),mj=(A&B)^(A&C)^(B&C),t2=(S0+mj)|0;
        Hh=G;G=F;F=E;E=(D+t1)|0;D=C;C=B;B=A;A=(t1+t2)|0;}
      H[0]=(H[0]+A)|0;H[1]=(H[1]+B)|0;H[2]=(H[2]+C)|0;H[3]=(H[3]+D)|0;H[4]=(H[4]+E)|0;H[5]=(H[5]+F)|0;H[6]=(H[6]+G)|0;H[7]=(H[7]+Hh)|0;}
    var out=[];for(i=0;i<8;i++)for(j=3;j>=0;j--)out.push((H[i]>>>(j*8))&255);return out;
  }
  function clean(t){return String(t||'').normalize('NFKC').toUpperCase().replace(/[^0-9A-Z]/g,'').split('').filter(function(c){return AL.indexOf(c)>=0;}).join('');}
  function enc(bytes,len){var s='',v=0,bits=0,i=0;while(s.length<len){v=(v*256+bytes[i%bytes.length])%1e12;i++;s+=AL[v%31];v=Math.floor(v/31);}return s;}
  function normId(id){var c=clean(id);return c.length===8?c:null;}
  function fmtId(id){return id.slice(0,4)+'-'+id.slice(4);}
  function newId(){var a=new Uint32Array(8),s='';(globalThis.crypto||{}).getRandomValues?crypto.getRandomValues(a):a.forEach(function(_,i){a[i]=Math.random()*4294967296;});for(var i=0;i<8;i++)s+=AL[a[i]%31];return s;}
  function code(id){return enc(sha256(SECRET+'|'+VER+'|code|'+id),10);}           // 10 文字の短縮コード
  function fmtCode(c){return c.slice(0,5)+'-'+c.slice(5);}
  function positions(id){var h=sha256(SECRET+'|'+VER+'|pos|'+id),pos=[],k=0;while(pos.length<10){var p=h[k%32]%48;k++;if(k>=32&&k%32===0)h=sha256(h.join(','));if(pos.indexOf(p)<0)pos.push(p);}return pos;}
  function key48(id,rand){ // 48 文字のキー列（ランダムな文字の中に短縮コードを散りばめる）
    var c=code(id),pos=positions(id),r=rand||newId()+newId()+newId()+newId()+newId()+newId(),k=[];
    for(var i=0;i<48;i++)k.push(AL[(AL.indexOf(r[i%r.length])+i*7)%31]);
    for(i=0;i<10;i++)k[pos[i]]=c[i];
    return k.join('').match(/.{4}/g).join('-');
  }
  function check(input,id){ // 登録テキスト全体・キー列・短縮コードのどれを貼っても照合できる
    id=normId(id);if(!id)return false;var t=String(input||''),c=code(id);
    var m=t.match(/KEY\s*[:：]\s*([0-9A-Za-z\-\s]{48,90})/);
    if(m){var k=clean(m[1]).slice(0,48);if(k.length===48){var pos=positions(id),x='';for(var i=0;i<10;i++)x+=k[pos[i]];if(x===c)return true;}}
    var s=clean(t);if(s.length===10&&s===c)return true;
    if(s.length===48){var pos2=positions(id),y='';for(var j=0;j<10;j++)y+=s[pos2[j]];return y===c;}
    return false;
  }
  return {AL:AL,sha256:sha256,normId:normId,fmtId:fmtId,newId:newId,code:code,fmtCode:fmtCode,key48:key48,check:check};
})();
