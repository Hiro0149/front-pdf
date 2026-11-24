# -*- coding: utf-8 -*-
# columns: ja ¦ en ¦ zhCN ¦ zhTW ¦ pt ¦ fr ¦ ko
import json
L=['en','zhCN','zhTW','pt','fr','ko']
EX=r"""
Front PDF の使い方¦Front PDF Help¦Front PDF 使用说明¦Front PDF 使用說明¦Ajuda do Front PDF¦Aide de Front PDF¦Front PDF 사용법
スキン¦Skin¦皮肤¦外觀¦Tema¦Thème¦스킨
ダーク¦Dark¦深色¦深色¦Escuro¦Sombre¦다크
レトロPC¦Retro PC¦复古PC¦復古PC¦PC retrô¦PC rétro¦레트로 PC
アクア¦Aqua¦Aqua¦Aqua¦Aqua¦Aqua¦아쿠아
ゲーム機¦Handheld¦掌机¦掌機¦Portátil¦Console¦게임기
もふもふ¦Fluffy pets¦毛茸茸¦毛茸茸¦Fofinho¦Tout doux¦몽글몽글
画像取込¦Image import¦图片导入¦圖片匯入¦Importar imagem¦Import d'image¦이미지 가져오기
PNG/JPEGを開いたときの配置¦Layout when opening PNG/JPEG¦打开PNG/JPEG时的排版¦開啟PNG/JPEG時的排版¦Layout ao abrir PNG/JPEG¦Mise en page à l'ouverture des PNG/JPEG¦PNG/JPEG를 열 때의 배치
星¦Star¦星形¦星形¦Estrela¦Étoile¦별
表¦Table¦表格¦表格¦Tabela¦Tableau¦표
行数¦Rows¦行数¦列數¦Linhas¦Lignes¦행 수
列数¦Columns¦列数¦欄數¦Colunas¦Colonnes¦열 수
チェック（✓）¦Check mark (✓)¦勾选（✓）¦勾選（✓）¦Marca de verificação (✓)¦Coche (✓)¦체크 표시 (✓)
画像を貼り付けました（ドラッグで移動・四隅で拡大縮小、Shift+四隅で縦横比を変更）¦Image pasted (drag to move, corners to resize, Shift+corner to change aspect ratio)¦已粘贴图片（拖动移动，拖四角缩放，Shift+四角改变比例）¦已貼上圖片（拖曳移動，拖四角縮放，Shift+四角改變比例）¦Imagem colada (arraste para mover, cantos para redimensionar, Shift+canto muda a proporção)¦Image collée (glissez pour déplacer, coins pour redimensionner, Maj+coin pour changer les proportions)¦이미지를 붙여넣었습니다 (드래그로 이동, 모서리로 크기 조절, Shift+모서리로 비율 변경)
画像の貼り付け¦Pasting images¦粘贴图片¦貼上圖片¦Colar imagens¦Coller des images¦이미지 붙여넣기
絵文字¦Emoji¦表情符号¦表情符號¦Emoji¦Émoji¦이모지
よく使う¦Frequently used¦常用¦常用¦Mais usados¦Fréquents¦자주 사용
顔¦Faces¦表情¦表情¦Rostos¦Visages¦얼굴
仕事・物流¦Work & logistics¦工作·物流¦工作·物流¦Trabalho e logística¦Travail et logistique¦업무·물류
記号¦Symbols¦符号¦符號¦Símbolos¦Symboles¦기호
その他の絵文字（Win + . で入力・貼り付け可）¦Other emoji (type with Win + . or paste)¦其他表情符号（可用 Win + . 输入或粘贴）¦其他表情符號（可用 Win + . 輸入或貼上）¦Outros emoji (Win + . ou colar)¦Autres émojis (Win + . ou coller)¦다른 이모지 (Win + . 로 입력·붙여넣기 가능)
右のパネルで絵文字を選んで、置きたい位置をクリック¦Pick an emoji in the right panel, then click where to place it¦在右侧面板选择表情符号，然后点击要放置的位置¦在右側面板選擇表情符號，然後點擊要放置的位置¦Escolha um emoji no painel à direita e clique onde colocá-lo¦Choisissez un émoji dans le panneau de droite puis cliquez où le placer¦오른쪽 패널에서 이모지를 골라 놓을 위치를 클릭
絵文字を置きました（クリックで続けて置けます。Escで選択ツール）¦Emoji placed (click to keep placing; Esc for the Select tool)¦已放置表情符号（点击可继续放置，按Esc切换到选择工具）¦已放置表情符號（點擊可繼續放置，按Esc切換到選取工具）¦Emoji colocado (clique para continuar; Esc para Selecionar)¦Émoji placé (cliquez pour continuer ; Échap pour l'outil Sélection)¦이모지를 놓았습니다 (클릭으로 계속 놓기, Esc로 선택 도구)
2ページ表示¦Two-page view¦双页显示¦雙頁顯示¦Duas páginas¦Deux pages¦2페이지 보기
AI向けの説明をコピー¦Copy manual for AI¦复制给AI的说明¦複製給AI的說明¦Copiar manual para IA¦Copier le manuel pour l'IA¦AI용 설명 복사
説明書を保存 (.md)¦Save manual (.md)¦保存说明书 (.md)¦儲存說明書 (.md)¦Salvar manual (.md)¦Enregistrer le manuel (.md)¦설명서 저장 (.md)
AI（Copilot・Claude など）に貼り付けて質問できる詳しい説明をコピー¦Copy the detailed manual to paste into an AI (Copilot, Claude, etc.) and ask questions¦复制详细说明，可粘贴到AI（Copilot、Claude等）中提问¦複製詳細說明，可貼到AI（Copilot、Claude等）中提問¦Copiar o manual detalhado para colar numa IA (Copilot, Claude etc.) e fazer perguntas¦Copier le manuel détaillé pour le coller dans une IA (Copilot, Claude, etc.)¦AI(Copilot·Claude 등)에 붙여넣어 질문할 수 있는 상세 설명 복사
詳しい説明書をテキスト(Markdown)で保存¦Save the detailed manual as text (Markdown)¦将详细说明书保存为文本（Markdown）¦將詳細說明書儲存為文字（Markdown）¦Salvar o manual detalhado como texto (Markdown)¦Enregistrer le manuel détaillé en texte (Markdown)¦상세 설명서를 텍스트(Markdown)로 저장
説明書をコピーしました。AIのチャットに貼り付けて質問できます¦Manual copied. Paste it into an AI chat to ask questions¦已复制说明书，可粘贴到AI聊天中提问¦已複製說明書，可貼到AI聊天中提問¦Manual copiado. Cole num chat de IA para perguntar¦Manuel copié. Collez-le dans une IA pour poser vos questions¦설명서를 복사했습니다. AI 채팅에 붙여넣어 질문할 수 있습니다
コピーできませんでした¦Couldn't copy¦无法复制¦無法複製¦Não foi possível copiar¦Copie impossible¦복사하지 못했습니다
コピー¦Copy¦复制¦複製¦Copiar¦Copier¦복사
コピーしました¦Copied¦已复制¦已複製¦Copiado¦Copié¦복사했습니다
Front PDF について¦About Front PDF¦关于 Front PDF¦關於 Front PDF¦Sobre o Front PDF¦À propos de Front PDF¦Front PDF 정보
バージョン・ライセンス¦Version & license¦版本与许可¦版本與授權¦Versão e licença¦Version et licence¦버전·라이선스
公式配布元¦Official source¦官方发布处¦官方發布處¦Fonte oficial¦Source officielle¦공식 배포처
改変されていないかの確認（SHA-256）¦Check that the file is unmodified (SHA-256)¦确认文件未被修改（SHA-256）¦確認檔案未被修改（SHA-256）¦Verificar se o arquivo não foi alterado (SHA-256)¦Vérifier que le fichier n'a pas été modifié (SHA-256)¦수정 여부 확인 (SHA-256)
MIT ライセンス全文¦MIT License (full text)¦MIT 许可全文¦MIT 授權全文¦Licença MIT (texto completo)¦Licence MIT (texte complet)¦MIT 라이선스 전문
サードパーティのライセンス¦Third-party licenses¦第三方许可¦第三方授權¦Licenças de terceiros¦Licences tierces¦서드파티 라이선스
GitHub Releases（公開準備中）¦GitHub Releases (coming soon)¦GitHub Releases（准备公开中）¦GitHub Releases（準備公開中）¦GitHub Releases (em breve)¦GitHub Releases (bientôt)¦GitHub Releases (공개 준비 중)
花まる¦Hanamaru (flower circle)¦花丸（表扬）¦花丸（表揚）¦Hanamaru (flor de elogio)¦Hanamaru (fleur de félicitation)¦꽃동그라미 (칭찬 도장)
コンテナ積み付け最適化ソフト（業務用）¦Container loading optimizer (for business)¦集装箱装载优化软件（商用）¦貨櫃裝載最佳化軟體（商用）¦Otimizador de carregamento de contêineres (uso profissional)¦Optimiseur de chargement de conteneurs (professionnel)¦컨테이너 적재 최적화 소프트웨어 (업무용)
人に勧めるときは¦Recommending it to others¦推荐给他人时¦推薦給他人時¦Para recomendar a outras pessoas¦Pour le recommander¦다른 사람에게 추천할 때
紹介文と URL をコピー¦Copy intro text and URL¦复制介绍文字和 URL¦複製介紹文字與 URL¦Copiar texto e URL¦Copier le texte et l'URL¦소개 문구와 URL 복사
Front Softworks のほかのソフト¦Other software by Front Softworks¦Front Softworks 的其他软件¦Front Softworks 的其他軟體¦Outros softwares da Front Softworks¦Autres logiciels de Front Softworks¦Front Softworks의 다른 소프트웨어
ようこそ Front PDF へ¦Welcome to Front PDF¦欢迎使用 Front PDF¦歡迎使用 Front PDF¦Bem-vindo ao Front PDF¦Bienvenue dans Front PDF¦Front PDF에 오신 것을 환영합니다
はじめる¦Get started¦开始使用¦開始使用¦Começar¦Commencer¦시작하기
無料・オフラインの PDF 編集ツール「Front PDF」（インストール不要・ファイルは外部に送信されません）¦Front PDF — a free, offline PDF editor (no installation; files never leave your PC)¦免费离线 PDF 编辑工具「Front PDF」（无需安装，文件不会发送到外部）¦免費離線 PDF 編輯工具「Front PDF」（無需安裝，檔案不會傳送到外部）¦Front PDF — editor de PDF gratuito e offline (sem instalação; os arquivos não saem do seu PC)¦Front PDF — éditeur PDF gratuit et hors ligne (sans installation ; vos fichiers ne quittent pas votre PC)¦무료 오프라인 PDF 편집 도구 「Front PDF」(설치 불필요, 파일은 외부로 전송되지 않음)
紹介文と URL をコピーしました。メールやチャットに貼り付けてください¦Intro text and URL copied. Paste them into an email or chat¦已复制介绍文字和 URL，请粘贴到邮件或聊天中¦已複製介紹文字與 URL，請貼到郵件或聊天中¦Texto e URL copiados. Cole-os num e-mail ou chat¦Texte et URL copiés. Collez-les dans un e-mail ou une discussion¦소개 문구와 URL을 복사했습니다. 메일이나 채팅에 붙여넣으세요
URL をコピー¦Copy URL¦复制 URL¦複製 URL¦Copiar URL¦Copier l'URL¦URL 복사
合言葉¦Passphrase¦口令¦通關密語¦Senha¦Mot de passe¦암호
合言葉が違います。公式配布元のページで確認してください¦Wrong passphrase. Please check it on the official source page¦口令不正确，请在官方发布处的页面上确认¦通關密語不正確，請在官方發布處的頁面上確認¦Senha incorreta. Confira na página da fonte oficial¦Mot de passe incorrect. Vérifiez-le sur la page de la source officielle¦암호가 틀렸습니다. 공식 배포처 페이지에서 확인하세요
合言葉を入力してください¦Please enter the passphrase¦请输入口令¦請輸入通關密語¦Digite a senha¦Saisissez le mot de passe¦암호를 입력하세요
ありがとうございます。Front PDF をお使いいただけます¦Thank you! Front PDF is ready to use¦谢谢！现在可以使用 Front PDF 了¦謝謝！現在可以使用 Front PDF 了¦Obrigado! O Front PDF está pronto para usar¦Merci ! Front PDF est prêt¦감사합니다! 이제 Front PDF를 사용할 수 있습니다
このブラウザの ID¦This browser's ID¦本浏览器的 ID¦本瀏覽器的 ID¦ID deste navegador¦ID de ce navigateur¦이 브라우저의 ID
ID をコピー¦Copy ID¦复制 ID¦複製 ID¦Copiar ID¦Copier l'ID¦ID 복사
公式ページの「アクティベーション」に ID を貼り付けて「発行する」¦Paste the ID into "Activation" on the official page and press "Issue"¦将 ID 粘贴到官方页面的"激活"中并点击"发放"¦將 ID 貼到官方頁面的「啟用」中並點選「發放」¦Cole o ID em "Ativação" na página oficial e clique em "Emitir"¦Collez l'ID dans « Activation » sur la page officielle et cliquez sur « Émettre »¦공식 페이지의 "활성화"에 ID를 붙여넣고 "발급" 클릭
公式ページを開いて、表示されたパスワードをコピー¦Open the official page and copy the password shown¦打开官方页面，复制显示的密码¦開啟官方頁面，複製顯示的密碼¦Abra a página oficial e copie a senha exibida¦Ouvrez la page officielle et copiez le mot de passe affiché¦공식 페이지를 열고 표시된 비밀번호 복사
公式ページを開く（パスワードがすぐ表示されます）¦Open the official page (the password appears right away)¦打开官方页面（密码会立即显示）¦開啟官方頁面（密碼會立即顯示）¦Abrir a página oficial (a senha aparece na hora)¦Ouvrir la page officielle (le mot de passe s'affiche aussitôt)¦공식 페이지 열기(비밀번호가 바로 표시됩니다)
ID が入っていないときは、1 の ID を貼り付けて「発行する」を押してください¦If the ID isn't filled in, paste the ID from step 1 and press "Issue"¦如果没有填入 ID，请粘贴第 1 步的 ID 并点击"发放"¦如果沒有填入 ID，請貼上第 1 步的 ID 並點選「發放」¦Se o ID não estiver preenchido, cole o ID do passo 1 e clique em "Emitir"¦Si l'ID n'est pas rempli, collez l'ID de l'étape 1 et cliquez sur « Émettre »¦ID가 입력되지 않았다면 1단계의 ID를 붙여넣고 "발급" 클릭
パスワードを下の欄に貼り付けて「はじめる」¦Paste the password in the box below and press "Get started"¦将密码粘贴到下方输入框并点击"开始使用"¦將密碼貼到下方欄位並點選「開始使用」¦Cole a senha no campo abaixo e clique em "Começar"¦Collez le mot de passe dans la zone ci-dessous et cliquez sur « Commencer »¦비밀번호를 아래 칸에 붙여넣고 "시작하기" 클릭
スマホで読み取ると、ID 入力済みの公式ページが開きます¦Scan with a phone to open the official page with the ID filled in¦用手机扫描即可打开已填好 ID 的官方页面¦用手機掃描即可開啟已填好 ID 的官方頁面¦Leia com o celular para abrir a página oficial com o ID preenchido¦Scannez avec un téléphone pour ouvrir la page officielle avec l'ID déjà rempli¦스마트폰으로 읽으면 ID가 입력된 공식 페이지가 열립니다
パスワード（または 10 文字の短いパスワード）をここに貼り付け¦Paste the password (or the 10-character short password) here¦在此粘贴密码（或 10 位短密码）¦在此貼上密碼（或 10 位短密碼）¦Cole aqui a senha (ou a senha curta de 10 caracteres)¦Collez ici le mot de passe (ou le mot de passe court à 10 caractères)¦비밀번호(또는 10자 짧은 비밀번호)를 여기에 붙여넣기
パスワードを貼り付けてください¦Please paste the password¦请粘贴密码¦請貼上密碼¦Cole a senha¦Collez le mot de passe¦비밀번호를 붙여넣으세요
このブラウザの ID 用のパスワードではありません。公式ページで発行し直してください¦This password is not for this browser's ID. Please issue it again on the official page¦这不是本浏览器 ID 的密码，请在官方页面重新发放¦這不是本瀏覽器 ID 的密碼，請在官方頁面重新發放¦Esta senha não é para o ID deste navegador. Emita de novo na página oficial¦Ce mot de passe ne correspond pas à l'ID de ce navigateur. Obtenez-le à nouveau sur la page officielle¦이 브라우저의 ID용 비밀번호가 아닙니다. 공식 페이지에서 다시 발급하세요
準備完了¦Ready¦就绪¦就緒¦Pronto¦Prêt¦준비 완료
開く¦Open¦打开¦開啟¦Abrir¦Ouvrir¦열기
作業を保存¦Save work¦保存工作¦儲存工作¦Salvar trabalho¦Enregistrer¦작업 저장
ファイル¦File¦文件¦檔案¦Arquivo¦Fichier¦파일
表示¦View¦视图¦檢視¦Exibir¦Affichage¦보기
ページ¦Page¦页面¦頁面¦Página¦Page¦페이지
書き出し¦Export¦导出¦匯出¦Exportar¦Exporter¦내보내기
倍率¦Zoom¦缩放¦縮放¦Zoom¦Zoom¦배율
検索¦Search¦搜索¦搜尋¦Buscar¦Rechercher¦검색
全体¦All pages¦全部¦全部¦Todas¦Toutes¦전체
▦ 一覧¦▦ Grid¦▦ 网格¦▦ 網格¦▦ Grade¦▦ Grille¦▦ 목록
✎ 編集¦✎ Edit¦✎ 编辑¦✎ 編輯¦✎ Editar¦✎ Éditer¦✎ 편집
⚙ 設定¦⚙ Settings¦⚙ 设置¦⚙ 設定¦⚙ Config.¦⚙ Réglages¦⚙ 설정
設定¦Settings¦设置¦設定¦Configurações¦Réglages¦설정
白紙追加¦Add blank¦添加空白页¦新增空白頁¦Pág. em branco¦Page vierge¦빈 페이지
複製¦Duplicate¦复制¦複製¦Duplicar¦Dupliquer¦복제
ページ削除¦Delete page¦删除页面¦刪除頁面¦Excluir página¦Suppr. page¦페이지 삭제
元に戻す¦Undo¦撤销¦復原¦Desfazer¦Annuler¦실행 취소
やり直し¦Redo¦重做¦重做¦Refazer¦Rétablir¦다시 실행
PNG書き出し¦Export PNG¦导出PNG¦匯出PNG¦Exportar PNG¦Exporter PNG¦PNG 내보내기
PDF書き出し¦Export PDF¦导出PDF¦匯出PDF¦Exportar PDF¦Exporter PDF¦PDF 내보내기
全てマーカー¦Highlight all¦全部高亮¦全部醒目¦Destacar tudo¦Tout surligner¦모두 강조
全て黒塗り¦Black out all¦全部涂黑¦全部塗黑¦Tarjar tudo¦Tout noircir¦모두 검게
透かし¦Watermark¦水印¦浮水印¦Marca d'água¦Filigrane¦워터마크
書き込み全消去¦Clear markups¦清除标注¦清除標註¦Limpar anotações¦Effacer annotations¦주석 모두 지우기
使い方¦Help¦帮助¦說明¦Ajuda¦Aide¦사용법
ページ全体¦Fit page¦整页¦整頁¦Página inteira¦Page entière¦페이지 전체
ページ幅¦Fit width¦页宽¦頁寬¦Largura da página¦Largeur de page¦페이지 너비
大きさ¦Size¦大小¦大小¦Tamanho¦Taille¦크기
列¦Columns¦列数¦欄數¦Colunas¦Colonnes¦열
自動¦Auto¦自动¦自動¦Auto¦Auto¦자동
選択¦Select¦选择¦選取¦Selecionar¦Sélection¦선택
文字選択¦Select text¦选字¦選字¦Sel. texto¦Sél. texte¦텍스트 선택
描く¦Draw¦绘制¦繪製¦Desenhar¦Dessiner¦그리기
図形¦Shapes¦图形¦圖形¦Formas¦Formes¦도형
塗る・隠す¦Fill / Hide¦填充·遮盖¦填色·遮蓋¦Preencher/Ocultar¦Remplir/Masquer¦칠하기·가리기
入れる¦Insert¦插入¦插入¦Inserir¦Insérer¦넣기
ペン¦Pen¦笔¦筆¦Caneta¦Stylo¦펜
ブラシ¦Brush¦毛笔¦毛筆¦Pincel¦Pinceau¦붓
蛍光ペン¦Marker pen¦荧光笔¦螢光筆¦Marca-texto¦Stylo fluo¦형광펜
消しゴム¦Eraser¦橡皮擦¦橡皮擦¦Borracha¦Gomme¦지우개
四角¦Box¦矩形¦矩形¦Caixa¦Cadre¦사각형
丸¦Ellipse¦椭圆¦橢圓¦Elipse¦Ellipse¦원
線¦Line¦直线¦直線¦Linha¦Ligne¦선
矢印¦Arrow¦箭头¦箭頭¦Seta¦Flèche¦화살표
マーカー¦Highlight¦高亮¦醒目¦Destaque¦Surligner¦강조
白塗り¦White-out¦涂白¦塗白¦Branco¦Blanc¦흰색 칠
黒塗り¦Black-out¦涂黑¦塗黑¦Tarja¦Noircir¦검게 칠
バケツ¦Fill¦油漆桶¦油漆桶¦Balde¦Remplir¦채우기
スポイト¦Color picker¦吸管¦滴管¦Conta-gotas¦Pipette¦스포이트
文字¦Text¦文字¦文字¦Texto¦Texte¦텍스트
付箋¦Sticky note¦便签¦便利貼¦Nota adesiva¦Note¦메모지
ハンコ¦Stamp¦印章¦印章¦Carimbo¦Tampon¦도장
画像¦Image¦图片¦圖片¦Imagem¦Image¦이미지
選択ツール¦Select tool¦选择工具¦選取工具¦Ferramenta Selecionar¦Outil Sélection¦선택 도구
お待ちください¦Please wait¦请稍候¦請稍候¦Aguarde¦Veuillez patienter¦잠시 기다려 주세요
処理中...¦Processing...¦处理中...¦處理中...¦Processando...¦Traitement...¦처리 중...
お知らせ¦Notice¦提示¦提示¦Aviso¦Information¦알림
OK¦OK¦确定¦確定¦OK¦OK¦확인
キャンセル¦Cancel¦取消¦取消¦Cancelar¦Annuler¦취소
閉じる¦Close¦关闭¦關閉¦Fechar¦Fermer¦닫기
保存¦Save¦保存¦儲存¦Salvar¦Enregistrer¦저장
出力方法¦Output¦输出方式¦輸出方式¦Saída¦Sortie¦출력 방법
全ページを1つのPDFに（結合）¦All pages into one PDF (merge)¦所有页面合并为一个PDF¦所有頁面合併為一個PDF¦Todas as páginas em um PDF (mesclar)¦Toutes les pages en un PDF (fusion)¦모든 페이지를 하나의 PDF로 (병합)
選択したページだけ¦Selected pages only¦仅所选页面¦僅選取的頁面¦Somente páginas selecionadas¦Pages sélectionnées uniquement¦선택한 페이지만
1ページずつ別ファイルに分割¦Split into one file per page¦每页拆分为单独文件¦每頁分割為單獨檔案¦Dividir em um arquivo por página¦Diviser en un fichier par page¦페이지마다 별도 파일로 분할
ページごとに分割¦pages per file¦页拆分为一个文件¦頁分割為一個檔案¦páginas por arquivo¦pages par fichier¦페이지씩 분할
範囲で分割¦Split by ranges¦按范围拆分¦依範圍分割¦Dividir por intervalos¦Diviser par plages¦범위로 분할
例: 1-3, 4-6, 7¦e.g. 1-3, 4-6, 7¦例：1-3, 4-6, 7¦例：1-3, 4-6, 7¦ex.: 1-3, 4-6, 7¦ex. : 1-3, 4-6, 7¦예: 1-3, 4-6, 7
ページ調整¦Page adjustments¦页面调整¦頁面調整¦Ajustes de página¦Ajustements de page¦페이지 조정
すべてA4サイズに揃える（向きはそのまま）¦Resize all to A4 (keep orientation)¦全部统一为A4（方向不变）¦全部統一為A4（方向不變）¦Ajustar tudo para A4 (mantém orientação)¦Tout mettre en A4 (orientation conservée)¦모두 A4로 맞추기 (방향 유지)
余白トリミング¦Trim margins¦裁剪边距¦裁切邊距¦Cortar margens¦Rogner les marges¦여백 자르기
mm（四辺）¦mm (all sides)¦mm（四边）¦mm（四邊）¦mm (todos os lados)¦mm (4 côtés)¦mm (네 변)
まとめ印刷¦N-up¦多页合一¦多頁合一¦Várias por folha¦Pages par feuille¦모아 찍기
なし¦None¦无¦無¦Nenhum¦Aucun¦없음
2in1（A4横に2ページ）¦2-up (2 pages on landscape A4)¦2合1（A4横向2页）¦2合1（A4橫向2頁）¦2 por folha (A4 paisagem)¦2 par feuille (A4 paysage)¦2-in-1 (A4 가로에 2페이지)
4in1（A4縦に4ページ）¦4-up (4 pages on portrait A4)¦4合1（A4纵向4页）¦4合1（A4直向4頁）¦4 por folha (A4 retrato)¦4 par feuille (A4 portrait)¦4-in-1 (A4 세로에 4페이지)
ファイル名¦File name¦文件名¦檔名¦Nome do arquivo¦Nom du fichier¦파일 이름
文書タイトル¦Document title¦文档标题¦文件標題¦Título do documento¦Titre du document¦문서 제목
（任意）¦(optional)¦（可选）¦（選填）¦(opcional)¦(facultatif)¦(선택)
PNG画像で書き出し¦Export as PNG images¦导出为PNG图片¦匯出為PNG圖片¦Exportar como imagens PNG¦Exporter en images PNG¦PNG 이미지로 내보내기
対象¦Target¦对象¦對象¦Alvo¦Cible¦대상
選択したページ¦Selected pages¦所选页面¦選取的頁面¦Páginas selecionadas¦Pages sélectionnées¦선택한 페이지
全ページ¦All pages¦全部页面¦全部頁面¦Todas as páginas¦Toutes les pages¦모든 페이지
解像度¦Resolution¦分辨率¦解析度¦Resolução¦Résolution¦해상도
96 dpi（画面用）¦96 dpi (screen)¦96 dpi（屏幕）¦96 dpi（螢幕）¦96 dpi (tela)¦96 dpi (écran)¦96 dpi (화면용)
150 dpi（標準）¦150 dpi (standard)¦150 dpi（标准）¦150 dpi（標準）¦150 dpi (padrão)¦150 dpi (standard)¦150 dpi (표준)
300 dpi（印刷用）¦300 dpi (print)¦300 dpi（打印）¦300 dpi（列印）¦300 dpi (impressão)¦300 dpi (impression)¦300 dpi (인쇄용)
書き出し前の確認¦Before exporting¦导出前确认¦匯出前確認¦Antes de exportar¦Avant l'export¦내보내기 전 확인
黒塗り・白塗りなどで隠した部分があります¦Some areas are hidden with black-out / white-out¦有用涂黑/涂白等遮盖的部分¦有以塗黑／塗白等遮蓋的部分¦Há áreas ocultadas com tarja preta/branca¦Certaines zones sont masquées (noir/blanc)¦검게/흰색 칠 등으로 가린 부분이 있습니다
塗ったページを画像化してPDF出力（推奨）¦Rasterize masked pages and export PDF (recommended)¦将涂抹的页面转为图像后导出PDF（推荐）¦將塗抹的頁面轉為影像後匯出PDF（建議）¦Converter páginas tarjadas em imagem e exportar PDF (recomendado)¦Convertir les pages masquées en image et exporter (recommandé)¦칠한 페이지를 이미지로 바꿔 PDF 출력 (권장)
PNGで書き出す¦Export as PNG¦导出为PNG¦匯出為PNG¦Exportar como PNG¦Exporter en PNG¦PNG로 내보내기
このまま書き出す¦Export as is¦直接导出¦直接匯出¦Exportar assim mesmo¦Exporter tel quel¦그대로 내보내기
次回からこの確認を表示しない¦Don't show this again¦下次不再显示¦下次不再顯示¦Não mostrar novamente¦Ne plus afficher¦다음부터 표시하지 않기
言語 / Language¦Language / 言語¦语言 / Language¦語言 / Language¦Idioma / Language¦Langue / Language¦언어 / Language
スキン（見た目）¦Skin (appearance)¦皮肤（外观）¦外觀主題¦Tema (aparência)¦Thème (apparence)¦스킨 (외관)
モダン¦Modern¦现代¦現代¦Moderno¦Moderne¦모던
モダン（ダーク）¦Modern (dark)¦现代（深色）¦現代（深色）¦Moderno (escuro)¦Moderne (sombre)¦모던 (다크)
レトロPC（98風）¦Retro PC (98 style)¦复古PC（98风格）¦復古PC（98風格）¦PC retrô (estilo 98)¦PC rétro (style 98)¦레트로 PC (98 스타일)
アクア（初期OS X風）¦Aqua (early OS X style)¦Aqua（早期OS X风格）¦Aqua（早期OS X風格）¦Aqua (estilo OS X antigo)¦Aqua (style premier OS X)¦아쿠아 (초기 OS X 스타일)
ポケットゲーム機風¦Pocket game console¦掌机风格¦掌機風格¦Console portátil¦Console de poche¦휴대용 게임기 스타일
画像（PNG/JPEG）の取り込み方¦How to import images (PNG/JPEG)¦图片（PNG/JPEG）导入方式¦圖片（PNG/JPEG）匯入方式¦Importação de imagens (PNG/JPEG)¦Import des images (PNG/JPEG)¦이미지(PNG/JPEG) 가져오기 방식
A4に配置¦Place on A4¦放在A4上¦置於A4上¦Colocar em A4¦Placer sur A4¦A4에 배치
画像サイズのまま¦Keep image size¦保持图片尺寸¦保持圖片尺寸¦Manter tamanho da imagem¦Garder la taille de l'image¦이미지 크기 그대로
PDF / PNG / JPEG / 作業ファイル(.frontpdf) を開く (Ctrl+O)¦Open PDF / PNG / JPEG / work file (.frontpdf) (Ctrl+O)¦打开PDF / PNG / JPEG / 工作文件(.frontpdf) (Ctrl+O)¦開啟PDF / PNG / JPEG / 工作檔案(.frontpdf) (Ctrl+O)¦Abrir PDF / PNG / JPEG / arquivo de trabalho (.frontpdf) (Ctrl+O)¦Ouvrir PDF / PNG / JPEG / fichier de travail (.frontpdf) (Ctrl+O)¦PDF / PNG / JPEG / 작업 파일(.frontpdf) 열기 (Ctrl+O)
作業ファイル(.frontpdf)に保存して、あとで続きから編集 (Ctrl+S)¦Save to a work file (.frontpdf) to continue later (Ctrl+S)¦保存为工作文件(.frontpdf)，稍后继续编辑 (Ctrl+S)¦儲存為工作檔案(.frontpdf)，稍後繼續編輯 (Ctrl+S)¦Salvar em arquivo de trabalho (.frontpdf) para continuar depois (Ctrl+S)¦Enregistrer dans un fichier de travail (.frontpdf) pour reprendre plus tard (Ctrl+S)¦작업 파일(.frontpdf)로 저장해 나중에 이어서 편집 (Ctrl+S)
サムネイルだけを大きく並べてページを整理¦Show large thumbnails only to organize pages¦只显示大缩略图来整理页面¦只顯示大縮圖來整理頁面¦Mostrar só miniaturas grandes para organizar páginas¦Afficher seulement de grandes miniatures pour organiser¦큰 썸네일만 표시해 페이지 정리
左にサムネイル、右でページに書き込み¦Thumbnails on the left, annotate the page on the right¦左侧缩略图，右侧在页面上标注¦左側縮圖，右側在頁面上標註¦Miniaturas à esquerda, anotar a página à direita¦Miniatures à gauche, annoter la page à droite¦왼쪽 썸네일, 오른쪽에서 페이지에 주석
白紙のA4ページを追加¦Add a blank A4 page¦添加空白A4页面¦新增空白A4頁面¦Adicionar página A4 em branco¦Ajouter une page A4 vierge¦빈 A4 페이지 추가
選択ページを左に90°回転¦Rotate selected pages 90° left¦所选页面向左旋转90°¦選取頁面向左旋轉90°¦Girar páginas selecionadas 90° à esquerda¦Pivoter les pages sélectionnées de 90° à gauche¦선택 페이지를 왼쪽으로 90° 회전
選択ページを右に90°回転¦Rotate selected pages 90° right¦所选页面向右旋转90°¦選取頁面向右旋轉90°¦Girar páginas selecionadas 90° à direita¦Pivoter les pages sélectionnées de 90° à droite¦선택 페이지를 오른쪽으로 90° 회전
選択ページを複製¦Duplicate selected pages¦复制所选页面¦複製選取頁面¦Duplicar páginas selecionadas¦Dupliquer les pages sélectionnées¦선택 페이지 복제
選択ページを削除¦Delete selected pages¦删除所选页面¦刪除選取頁面¦Excluir páginas selecionadas¦Supprimer les pages sélectionnées¦선택 페이지 삭제
元に戻す (Ctrl+Z)¦Undo (Ctrl+Z)¦撤销 (Ctrl+Z)¦復原 (Ctrl+Z)¦Desfazer (Ctrl+Z)¦Annuler (Ctrl+Z)¦실행 취소 (Ctrl+Z)
やり直し (Ctrl+Y)¦Redo (Ctrl+Y)¦重做 (Ctrl+Y)¦重做 (Ctrl+Y)¦Refazer (Ctrl+Y)¦Rétablir (Ctrl+Y)¦다시 실행 (Ctrl+Y)
ページをPNG画像で書き出し¦Export pages as PNG images¦将页面导出为PNG图片¦將頁面匯出為PNG圖片¦Exportar páginas como imagens PNG¦Exporter les pages en images PNG¦페이지를 PNG 이미지로 내보내기
結合・分割・A4揃えなどを選んでPDFに書き出し¦Export PDF with merge, split, A4 resize, etc.¦选择合并、拆分、A4统一等方式导出PDF¦選擇合併、分割、A4統一等方式匯出PDF¦Exportar PDF com mesclar, dividir, ajustar A4 etc.¦Exporter en PDF : fusion, division, format A4, etc.¦병합·분할·A4 맞춤 등을 선택해 PDF로 내보내기
前のページ (PageUp)¦Previous page (PageUp)¦上一页 (PageUp)¦上一頁 (PageUp)¦Página anterior (PageUp)¦Page précédente (PageUp)¦이전 페이지 (PageUp)
次のページ (PageDown)¦Next page (PageDown)¦下一页 (PageDown)¦下一頁 (PageDown)¦Próxima página (PageDown)¦Page suivante (PageDown)¦다음 페이지 (PageDown)
縮小 (Ctrl+ホイール / Ctrl+－)¦Zoom out (Ctrl+wheel / Ctrl+-)¦缩小 (Ctrl+滚轮 / Ctrl+-)¦縮小 (Ctrl+滾輪 / Ctrl+-)¦Diminuir zoom (Ctrl+roda / Ctrl+-)¦Zoom arrière (Ctrl+molette / Ctrl+-)¦축소 (Ctrl+휠 / Ctrl+-)
拡大 (Ctrl+ホイール / Ctrl+＋)¦Zoom in (Ctrl+wheel / Ctrl++)¦放大 (Ctrl+滚轮 / Ctrl++)¦放大 (Ctrl+滾輪 / Ctrl++)¦Aumentar zoom (Ctrl+roda / Ctrl++)¦Zoom avant (Ctrl+molette / Ctrl++)¦확대 (Ctrl+휠 / Ctrl++)
表示倍率¦Zoom level¦显示比例¦顯示比例¦Nível de zoom¦Niveau de zoom¦표시 배율
文字検索 (Ctrl+F)¦Search text (Ctrl+F)¦搜索文字 (Ctrl+F)¦搜尋文字 (Ctrl+F)¦Buscar texto (Ctrl+F)¦Rechercher (Ctrl+F)¦텍스트 검색 (Ctrl+F)
Enterで検索・次へ／Shift+Enterで前へ¦Enter: search / next, Shift+Enter: previous¦Enter：搜索/下一个，Shift+Enter：上一个¦Enter：搜尋/下一個，Shift+Enter：上一個¦Enter: buscar/próximo, Shift+Enter: anterior¦Entrée : rechercher/suivant, Maj+Entrée : précédent¦Enter: 검색/다음, Shift+Enter: 이전
前へ (Shift+Enter)¦Previous (Shift+Enter)¦上一个 (Shift+Enter)¦上一個 (Shift+Enter)¦Anterior (Shift+Enter)¦Précédent (Maj+Entrée)¦이전 (Shift+Enter)
次へ (Enter)¦Next (Enter)¦下一个 (Enter)¦下一個 (Enter)¦Próximo (Enter)¦Suivant (Entrée)¦다음 (Enter)
見つかった全箇所に蛍光マーカーを引く¦Highlight every match¦高亮所有匹配处¦醒目標示所有符合處¦Destacar todas as ocorrências¦Surligner toutes les occurrences¦찾은 모든 곳에 형광 표시
見つかった全箇所を黒塗り¦Black out every match¦涂黑所有匹配处¦塗黑所有符合處¦Tarjar todas as ocorrências¦Noircir toutes les occurrences¦찾은 모든 곳을 검게 칠하기
全ページ共通の透かし文字¦Watermark text on all pages¦所有页面共用的水印文字¦所有頁面共用的浮水印文字¦Texto de marca d'água em todas as páginas¦Filigrane sur toutes les pages¦모든 페이지 공통 워터마크
表示中ページの書き込みを全部消す¦Remove all markups on this page¦删除当前页的全部标注¦刪除目前頁面的全部標註¦Remover todas as anotações desta página¦Supprimer toutes les annotations de cette page¦현재 페이지의 주석 모두 지우기
画像の取り込み方法・スキン（見た目）¦Image import & skin¦图片导入方式·皮肤¦圖片匯入方式·外觀¦Importação de imagens e tema¦Import d'images et thème¦이미지 가져오기·스킨
見た目を切り替え¦Change appearance¦切换外观¦切換外觀¦Mudar aparência¦Changer l'apparence¦외관 변경
サムネイルの大きさ（Ctrl+ホイールでも変更）¦Thumbnail size (also Ctrl+wheel)¦缩略图大小（也可Ctrl+滚轮）¦縮圖大小（也可Ctrl+滾輪）¦Tamanho das miniaturas (também Ctrl+roda)¦Taille des miniatures (aussi Ctrl+molette)¦썸네일 크기 (Ctrl+휠로도 변경)
横に並べる数¦Thumbnails per row¦每行数量¦每列數量¦Por linha¦Par ligne¦가로 개수
ドラッグで幅を調整¦Drag to resize¦拖动调整宽度¦拖曳調整寬度¦Arraste para redimensionar¦Glisser pour redimensionner¦드래그해서 폭 조정
ここに選択した文字が表示されます（編集してからコピーもできます）¦Selected text appears here (you can edit before copying)¦所选文字显示在这里（可编辑后再复制）¦選取的文字顯示在這裡（可編輯後再複製）¦O texto selecionado aparece aqui (pode editar antes de copiar)¦Le texte sélectionné s'affiche ici (modifiable avant copie)¦선택한 텍스트가 여기에 표시됩니다 (편집 후 복사 가능)
コピー (Ctrl+C)¦Copy (Ctrl+C)¦复制 (Ctrl+C)¦複製 (Ctrl+C)¦Copiar (Ctrl+C)¦Copier (Ctrl+C)¦복사 (Ctrl+C)
コピー形式¦Copy format¦复制格式¦複製格式¦Formato da cópia¦Format de copie¦복사 형식
表（タブ区切り・Excelに貼れる）¦Table (tab-separated, pastes into Excel)¦表格（制表符分隔，可粘贴到Excel）¦表格（Tab分隔，可貼到Excel）¦Tabela (separada por tab, cola no Excel)¦Tableau (tabulations, collable dans Excel)¦표 (탭 구분, Excel에 붙여넣기 가능)
文章（スペース区切り）¦Plain text (space-separated)¦文本（空格分隔）¦文字（空格分隔）¦Texto (separado por espaço)¦Texte (séparé par espaces)¦문장 (공백 구분)
ページ全体を選択¦Select whole page¦全选本页¦全選本頁¦Selecionar página inteira¦Tout sélectionner¦페이지 전체 선택
このページの文字をすべて選択 (Ctrl+A)¦Select all text on this page (Ctrl+A)¦选择本页全部文字 (Ctrl+A)¦選取本頁全部文字 (Ctrl+A)¦Selecionar todo o texto desta página (Ctrl+A)¦Sélectionner tout le texte de la page (Ctrl+A)¦이 페이지의 텍스트 모두 선택 (Ctrl+A)
選択解除¦Deselect¦取消选择¦取消選取¦Desmarcar¦Désélectionner¦선택 해제
文字選択・コピー¦Select & copy text¦选择·复制文字¦選取·複製文字¦Selecionar e copiar texto¦Sélectionner et copier¦텍스트 선택·복사
削除¦Delete¦删除¦刪除¦Excluir¦Supprimer¦삭제
最前面¦Bring to front¦置于顶层¦移至最上層¦Trazer p/ frente¦Premier plan¦맨 앞으로
最背面¦Send to back¦置于底层¦移至最下層¦Enviar p/ trás¦Arrière-plan¦맨 뒤로
全ページへ¦To all pages¦应用到所有页¦套用到所有頁¦Em todas as páginas¦Sur toutes les pages¦모든 페이지에
他の全ページの同じ位置にも入れる¦Also place at the same spot on all other pages¦在其他所有页面的相同位置也添加¦在其他所有頁面的相同位置也加入¦Colocar também na mesma posição das outras páginas¦Placer aussi au même endroit sur les autres pages¦다른 모든 페이지의 같은 위치에도 넣기
既定にする¦Set as default¦设为默认¦設為預設¦Definir como padrão¦Définir par défaut¦기본값으로
次から同じ設定で書き込む¦Use these settings next time¦下次使用相同设置¦下次使用相同設定¦Usar estas configurações da próxima vez¦Utiliser ces réglages la prochaine fois¦다음부터 같은 설정 사용
ハンコ帳に登録¦Add to stamp book¦加入印章簿¦加入印章簿¦Adicionar ao caderno¦Ajouter au carnet¦도장 모음에 등록
このハンコをハンコ帳に記憶する¦Save this stamp to the stamp book¦将此印章保存到印章簿¦將此印章儲存到印章簿¦Salvar este carimbo no caderno¦Enregistrer ce tampon dans le carnet¦이 도장을 도장 모음에 저장
ハンコ帳（自動で記憶）¦Stamp book (saved automatically)¦印章簿（自动保存）¦印章簿（自動儲存）¦Caderno de carimbos (salvo automaticamente)¦Carnet de tampons (enregistré automatiquement)¦도장 모음 (자동 저장)
新規¦New¦新建¦新增¦Novo¦Nouveau¦새로 만들기
画像から登録¦From image¦从图片添加¦從圖片新增¦A partir de imagem¦Depuis une image¦이미지로 등록
スキャンした印影などを登録（白は透明になります）¦Register a scanned seal etc. (white becomes transparent)¦添加扫描的印鉴等（白色变透明）¦新增掃描的印鑑等（白色變透明）¦Registrar um carimbo digitalizado (branco fica transparente)¦Ajouter un tampon numérisé (le blanc devient transparent)¦스캔한 인영 등록 (흰색은 투명해짐)
選んだハンコを編集¦Edit the selected stamp¦编辑所选印章¦編輯所選印章¦Editar o carimbo selecionado¦Modifier le tampon choisi¦선택한 도장 편집
書出（バックアップ）¦Export (backup)¦导出（备份）¦匯出（備份）¦Exportar (backup)¦Exporter (sauvegarde)¦내보내기 (백업)
ハンコ帳をファイルに保存（別のPCへの移行用）¦Save the stamp book to a file (to move to another PC)¦将印章簿保存为文件（用于迁移到其他电脑）¦將印章簿儲存為檔案（用於移轉到其他電腦）¦Salvar o caderno em arquivo (para outro PC)¦Enregistrer le carnet dans un fichier (pour un autre PC)¦도장 모음을 파일로 저장 (다른 PC로 옮기기용)
読込¦Import¦导入¦匯入¦Importar¦Importer¦불러오기
バックアップしたハンコ帳を追加で読み込む¦Import a backed-up stamp book¦导入备份的印章簿¦匯入備份的印章簿¦Importar um caderno salvo¦Importer un carnet sauvegardé¦백업한 도장 모음 불러오기
初期状態に戻す¦Reset¦恢复初始状态¦恢復初始狀態¦Restaurar padrão¦Réinitialiser¦초기화
種類¦Type¦类型¦類型¦Tipo¦Type¦종류
角枠スタンプ¦Box stamp¦方框印章¦方框印章¦Carimbo retangular¦Tampon rectangulaire¦사각 테두리 도장
二重枠スタンプ¦Double-box stamp¦双框印章¦雙框印章¦Carimbo de borda dupla¦Tampon double cadre¦이중 테두리 도장
小判型スタンプ¦Oval stamp¦椭圆印章¦橢圓印章¦Carimbo oval¦Tampon ovale¦타원 도장
丸印（縦書き）¦Round seal (vertical text)¦圆章（竖排）¦圓章（直書）¦Selo redondo (texto vertical)¦Sceau rond (texte vertical)¦원형 인 (세로쓰기)
日付印（3段）¦Date stamp (3 rows)¦日期章（三栏）¦日期章（三欄）¦Carimbo de data (3 linhas)¦Tampon dateur (3 lignes)¦날짜 도장 (3단)
角印¦Square seal¦方章¦方章¦Selo quadrado¦Sceau carré¦사각 인
画像（印影など）¦Image (scanned seal etc.)¦图片（印鉴等）¦圖片（印鑑等）¦Imagem (carimbo digitalizado)¦Image (tampon numérisé)¦이미지 (인영 등)
文字¦Text¦文字¦文字¦Texto¦Texte¦텍스트
日付を入れる¦Include date¦加入日期¦加入日期¦Incluir data¦Inclure la date¦날짜 넣기
押した日の日付にする¦Use the date when stamped¦使用盖章当天日期¦使用蓋章當天日期¦Usar a data do dia¦Utiliser la date du jour¦찍은 날 날짜 사용
日付¦Date¦日期¦日期¦Data¦Date¦날짜
日付の形式¦Date format¦日期格式¦日期格式¦Formato da data¦Format de date¦날짜 형식
色¦Color¦颜色¦顏色¦Cor¦Couleur¦색
上段¦Top row¦上栏¦上欄¦Linha superior¦Ligne du haut¦윗단
下段（空欄可）¦Bottom row (optional)¦下栏（可空）¦下欄（可空白）¦Linha inferior (opcional)¦Ligne du bas (facultatif)¦아랫단 (비워도 됨)
文字（1〜3字は縦書き）¦Text (1–3 chars are vertical)¦文字（1–3字竖排）¦文字（1–3字直書）¦Texto (1–3 caracteres na vertical)¦Texte (1–3 car. en vertical)¦텍스트 (1~3자는 세로쓰기)
文字（4字で2列・右から）¦Text (4 chars: 2 columns, right to left)¦文字（4字：两列，从右起）¦文字（4字：兩欄，從右起）¦Texto (4 caracteres: 2 colunas, da direita)¦Texte (4 car. : 2 colonnes, de droite)¦텍스트 (4자: 2열, 오른쪽부터)
直径 (mm)¦Diameter (mm)¦直径 (mm)¦直徑 (mm)¦Diâmetro (mm)¦Diamètre (mm)¦지름 (mm)
大きさ (mm)¦Size (mm)¦大小 (mm)¦大小 (mm)¦Tamanho (mm)¦Taille (mm)¦크기 (mm)
大きさ (pt)¦Size (pt)¦大小 (pt)¦大小 (pt)¦Tamanho (pt)¦Taille (pt)¦크기 (pt)
幅 (mm)¦Width (mm)¦宽度 (mm)¦寬度 (mm)¦Largura (mm)¦Largeur (mm)¦폭 (mm)
不透明度¦Opacity¦不透明度¦不透明度¦Opacidade¦Opacité¦불투명도
文字（改行OK）¦Text (line breaks OK)¦文字（可换行）¦文字（可換行）¦Texto (quebras de linha OK)¦Texte (retours à la ligne OK)¦텍스트 (줄바꿈 가능)
書体¦Font¦字体¦字型¦Fonte¦Police¦글꼴
ゴシック¦Sans-serif¦黑体¦黑體¦Sem serifa¦Sans serif¦고딕
明朝¦Serif¦宋体¦明體¦Serifa¦Serif¦명조
等幅¦Monospace¦等宽¦等寬¦Monoespaçada¦Chasse fixe¦고정폭
太字¦Bold¦粗体¦粗體¦Negrito¦Gras¦굵게
背景¦Background¦背景¦背景¦Fundo¦Fond¦배경
なし（透明）¦None (transparent)¦无（透明）¦無（透明）¦Nenhum (transparente)¦Aucun (transparent)¦없음 (투명)
白（下を隠す）¦White (hides below)¦白色（遮盖下方）¦白色（遮蓋下方）¦Branco (oculta o que está embaixo)¦Blanc (masque le dessous)¦흰색 (아래를 가림)
黄色¦Yellow¦黄色¦黃色¦Amarelo¦Jaune¦노란색
枠線あり¦Border¦有边框¦有邊框¦Borda¦Bordure¦테두리
枠線の色¦Border color¦边框颜色¦邊框顏色¦Cor da borda¦Couleur de bordure¦테두리 색
枠線の太さ¦Border width¦边框粗细¦邊框粗細¦Espessura da borda¦Épaisseur de bordure¦테두리 두께
塗りつぶし¦Fill¦填充¦填色¦Preenchimento¦Remplissage¦채우기
塗りの色¦Fill color¦填充颜色¦填色顏色¦Cor de preenchimento¦Couleur de remplissage¦채우기 색
太さ¦Width¦粗细¦粗細¦Espessura¦Épaisseur¦두께
矢印にする¦Arrow head¦带箭头¦帶箭頭¦Com seta¦Avec flèche¦화살표로
筆ペン（速さ・筆圧で太さが変わる）¦Brush pen (width varies with speed/pressure)¦毛笔（粗细随速度/压力变化）¦毛筆（粗細隨速度/壓力變化）¦Pincel (espessura varia com velocidade/pressão)¦Pinceau (épaisseur selon vitesse/pression)¦붓펜 (속도·필압으로 굵기 변화)
エアブラシ（ふちがぼける）¦Airbrush (soft edges)¦喷枪（边缘柔和）¦噴槍（邊緣柔和）¦Aerógrafo (bordas suaves)¦Aérographe (bords doux)¦에어브러시 (가장자리가 흐림)
塗る色¦Fill color¦填充颜色¦填色顏色¦Cor de preenchimento¦Couleur de remplissage¦칠할 색
不透明度（囲んだ範囲の塗り）¦Opacity (enclosed-area fill)¦不透明度（封闭区域填充）¦不透明度（封閉區域填色）¦Opacidade (preenchimento de área fechada)¦Opacité (remplissage de zone fermée)¦불투명도 (둘러싼 영역 채우기)
消しゴムの大きさ (pt)¦Eraser size (pt)¦橡皮擦大小 (pt)¦橡皮擦大小 (pt)¦Tamanho da borracha (pt)¦Taille de la gomme (pt)¦지우개 크기 (pt)
文字（付箋上をダブルクリックでも直接入力できます）¦Text (or double-click the note to type directly)¦文字（也可双击便签直接输入）¦文字（也可雙擊便利貼直接輸入）¦Texto (ou clique duas vezes na nota para digitar)¦Texte (ou double-cliquez sur la note)¦텍스트 (메모지를 더블클릭해 직접 입력 가능)
文字の大きさ (pt)¦Font size (pt)¦字号 (pt)¦字級 (pt)¦Tamanho da fonte (pt)¦Taille du texte (pt)¦글자 크기 (pt)
文字の色¦Text color¦文字颜色¦文字顏色¦Cor do texto¦Couleur du texte¦글자 색
付箋の色¦Note color¦便签颜色¦便利貼顏色¦Cor da nota¦Couleur de la note¦메모지 색
黄¦Yellow¦黄¦黃¦Amarelo¦Jaune¦노랑
ピンク¦Pink¦粉色¦粉紅¦Rosa¦Rose¦분홍
水色¦Light blue¦浅蓝¦淺藍¦Azul-claro¦Bleu clair¦하늘색
緑¦Green¦绿¦綠¦Verde¦Vert¦초록
オレンジ¦Orange¦橙色¦橘色¦Laranja¦Orange¦주황
紫¦Purple¦紫¦紫¦Roxo¦Violet¦보라
白¦White¦白¦白¦Branco¦Blanc¦흰색
作成者名（記憶されます）¦Author name (remembered)¦作者名（会被记住）¦作者名稱（會被記住）¦Nome do autor (memorizado)¦Nom de l'auteur (mémorisé)¦작성자 이름 (기억됨)
ページに焼き込む（受け取った人が移動・削除できなくなる）¦Burn into the page (recipients can't move or delete it)¦烧录到页面（接收者无法移动或删除）¦燒錄到頁面（接收者無法移動或刪除）¦Gravar na página (destinatário não pode mover/excluir)¦Incruster dans la page (non déplaçable/supprimable)¦페이지에 고정 (받는 사람이 이동·삭제 불가)
透かし（全ページ共通）¦Watermark (all pages)¦水印（所有页面通用）¦浮水印（所有頁面通用）¦Marca d'água (todas as páginas)¦Filigrane (toutes les pages)¦워터마크 (모든 페이지 공통)
透かしの文字¦Watermark text¦水印文字¦浮水印文字¦Texto da marca d'água¦Texte du filigrane¦워터마크 텍스트
角度 (°)¦Angle (°)¦角度 (°)¦角度 (°)¦Ângulo (°)¦Angle (°)¦각도 (°)
濃さ¦Strength¦浓度¦濃度¦Intensidade¦Intensité¦진하기
透かしを削除¦Remove watermark¦删除水印¦刪除浮水印¦Remover marca d'água¦Supprimer le filigrane¦워터마크 삭제
最近拾った色¦Recent colors¦最近拾取的颜色¦最近擷取的顏色¦Cores recentes¦Couleurs récentes¦최근 가져온 색
（なし：拾った色は次に選ぶツールに使われます）¦(none: the picked color will be used by the next tool you choose)¦（无：拾取的颜色将用于下一个选择的工具）¦（無：擷取的顏色將用於下一個選擇的工具）¦(nenhum: a cor será usada pela próxima ferramenta escolhida)¦(aucune : la couleur servira à l'outil choisi ensuite)¦(없음: 가져온 색은 다음에 고르는 도구에 사용)
白紙¦Blank¦空白页¦空白頁¦Em branco¦Vierge¦빈 페이지
0件¦0 hits¦0个¦0個¦0 resultados¦0 résultat¦0건
PDF・PNG・JPEG に対応しています。¦Supported: PDF, PNG, JPEG.¦支持PDF、PNG、JPEG。¦支援PDF、PNG、JPEG。¦Formatos aceitos: PDF, PNG, JPEG.¦Formats pris en charge : PDF, PNG, JPEG.¦PDF·PNG·JPEG를 지원합니다.
（パスワード付きPDFは開けません）¦(Password-protected PDFs cannot be opened)¦（无法打开带密码的PDF）¦（無法開啟有密碼的PDF）¦(PDFs protegidos por senha não podem ser abertos)¦(Les PDF protégés par mot de passe ne peuvent pas être ouverts)¦(암호가 걸린 PDF는 열 수 없습니다)
ブラウザだけで動くPDF加工ツールです。¦A PDF tool that runs entirely in your browser.¦一款完全在浏览器中运行的PDF工具。¦一款完全在瀏覽器中執行的PDF工具。¦Uma ferramenta de PDF que roda só no navegador.¦Un outil PDF qui fonctionne entièrement dans le navigateur.¦브라우저만으로 작동하는 PDF 편집 도구입니다.
ファイルは外部に送信されません。¦Your files are never sent anywhere.¦文件不会发送到外部。¦檔案不會傳送到外部。¦Seus arquivos nunca são enviados.¦Vos fichiers ne sont jamais envoyés.¦파일은 외부로 전송되지 않습니다.
これ以上元に戻せません¦Nothing more to undo¦无法再撤销¦無法再復原¦Nada mais para desfazer¦Rien d'autre à annuler¦더 이상 되돌릴 수 없습니다
元に戻しました¦Undone¦已撤销¦已復原¦Desfeito¦Annulé¦되돌렸습니다
やり直しました¦Redone¦已重做¦已重做¦Refeito¦Rétabli¦다시 실행했습니다
保存をキャンセルしました¦Save cancelled¦已取消保存¦已取消儲存¦Salvamento cancelado¦Enregistrement annulé¦저장을 취소했습니다
保存エラー¦Save error¦保存错误¦儲存錯誤¦Erro ao salvar¦Erreur d'enregistrement¦저장 오류
作業ファイルを開けません¦Can't open work file¦无法打开工作文件¦無法開啟工作檔案¦Não foi possível abrir o arquivo de trabalho¦Impossible d'ouvrir le fichier de travail¦작업 파일을 열 수 없습니다
Front PDFの作業ファイルではありません¦This is not a Front PDF work file¦这不是Front PDF的工作文件¦這不是Front PDF的工作檔案¦Este não é um arquivo de trabalho do Front PDF¦Ce n'est pas un fichier de travail Front PDF¦Front PDF의 작업 파일이 아닙니다
保存するページがありません。¦There are no pages to save.¦没有可保存的页面。¦沒有可儲存的頁面。¦Não há páginas para salvar.¦Aucune page à enregistrer.¦저장할 페이지가 없습니다.
作業ファイルを保存中...¦Saving work file...¦正在保存工作文件...¦正在儲存工作檔案...¦Salvando arquivo de trabalho...¦Enregistrement du fichier de travail...¦작업 파일 저장 중...
作業ファイルを開いています...¦Opening work file...¦正在打开工作文件...¦正在開啟工作檔案...¦Abrindo arquivo de trabalho...¦Ouverture du fichier de travail...¦작업 파일 여는 중...
画像エラー¦Image error¦图片错误¦圖片錯誤¦Erro de imagem¦Erreur d'image¦이미지 오류
画像を読み込めません¦Can't load the image¦无法读取图片¦無法讀取圖片¦Não foi possível carregar a imagem¦Impossible de charger l'image¦이미지를 불러올 수 없습니다
読み込みエラー¦Load error¦读取错误¦讀取錯誤¦Erro ao carregar¦Erreur de chargement¦불러오기 오류
読み込めません¦Can't open¦无法读取¦無法讀取¦Não foi possível abrir¦Impossible d'ouvrir¦열 수 없습니다
書き出しエラー¦Export error¦导出错误¦匯出錯誤¦Erro ao exportar¦Erreur d'export¦내보내기 오류
ページがありません¦No pages¦没有页面¦沒有頁面¦Sem páginas¦Aucune page¦페이지가 없습니다
ページがありません。¦There are no pages.¦没有页面。¦沒有頁面。¦Não há páginas.¦Aucune page.¦페이지가 없습니다.
先にファイルを開いてください。¦Please open a file first.¦请先打开文件。¦請先開啟檔案。¦Abra um arquivo primeiro.¦Ouvrez d'abord un fichier.¦먼저 파일을 열어 주세요.
ページが選択されていません。¦No pages are selected.¦未选择页面。¦未選取頁面。¦Nenhuma página selecionada.¦Aucune page sélectionnée.¦선택된 페이지가 없습니다.
範囲を入力してください（例: 1-3, 4-6）¦Enter ranges (e.g. 1-3, 4-6)¦请输入范围（例：1-3, 4-6）¦請輸入範圍（例：1-3, 4-6）¦Informe os intervalos (ex.: 1-3, 4-6)¦Saisissez les plages (ex. : 1-3, 4-6)¦범위를 입력하세요 (예: 1-3, 4-6)
白紙ページを追加しました¦Blank page added¦已添加空白页¦已新增空白頁¦Página em branco adicionada¦Page vierge ajoutée¦빈 페이지를 추가했습니다
透かしを削除しました¦Watermark removed¦已删除水印¦已刪除浮水印¦Marca d'água removida¦Filigrane supprimé¦워터마크를 삭제했습니다
透かしを選択中 ― 右のパネルで文字の変更・削除ができます（全ページ共通）¦Watermark selected — edit or remove it in the right panel (all pages)¦已选择水印 — 可在右侧面板修改或删除（所有页面通用）¦已選取浮水印 — 可在右側面板修改或刪除（所有頁面通用）¦Marca d'água selecionada — edite ou remova no painel à direita (todas as páginas)¦Filigrane sélectionné — modifiez-le ou supprimez-le dans le panneau de droite (toutes les pages)¦워터마크 선택 중 — 오른쪽 패널에서 수정·삭제 가능 (모든 페이지 공통)
線の上です。囲んだ内側をクリックしてください¦That's on a line. Click inside the enclosed area¦点在了线上。请点击封闭区域内侧¦點在了線上。請點擊封閉區域內側¦Isso é uma linha. Clique dentro da área fechada¦C'est sur un trait. Cliquez à l'intérieur de la zone fermée¦선 위입니다. 둘러싼 안쪽을 클릭하세요
囲んだ範囲を塗りつぶしました（Ctrl+Z で戻せます）¦Enclosed area filled (Ctrl+Z to undo)¦已填充封闭区域（可按Ctrl+Z撤销）¦已填滿封閉區域（可按Ctrl+Z復原）¦Área fechada preenchida (Ctrl+Z para desfazer)¦Zone fermée remplie (Ctrl+Z pour annuler)¦둘러싼 영역을 채웠습니다 (Ctrl+Z로 되돌리기)
囲まれた範囲ではありません。ペンなどで閉じた線の内側をクリックしてください（書き込みの色を変えるときは線や図形を直接クリック）¦Not an enclosed area. Click inside a closed line drawn with the pen etc. (to recolor a markup, click the line or shape itself)¦不是封闭区域。请点击用笔等画出的闭合线内侧（要改变标注颜色请直接点击线条或图形）¦不是封閉區域。請點擊用筆等畫出的閉合線內側（要改變標註顏色請直接點擊線條或圖形）¦Não é uma área fechada. Clique dentro de uma linha fechada desenhada com a caneta etc. (para mudar a cor, clique na própria linha ou forma)¦Zone non fermée. Cliquez à l'intérieur d'un tracé fermé (pour changer une couleur, cliquez directement sur le trait ou la forme)¦둘러싸인 영역이 아닙니다. 펜 등으로 닫은 선의 안쪽을 클릭하세요 (주석 색을 바꿀 때는 선이나 도형을 직접 클릭)
印影の画像は色を変えられません¦Can't recolor a seal image¦印鉴图片无法改色¦印鑑圖片無法改色¦Não é possível mudar a cor de uma imagem de carimbo¦Impossible de recolorer une image de tampon¦인영 이미지는 색을 바꿀 수 없습니다
貼り付けた画像は色を変えられません¦Can't recolor a pasted image¦粘贴的图片无法改色¦貼上的圖片無法改色¦Não é possível mudar a cor de uma imagem colada¦Impossible de recolorer une image collée¦붙여넣은 이미지는 색을 바꿀 수 없습니다
画像には色を設定できません¦Images can't take a color¦图片无法设置颜色¦圖片無法設定顏色¦Imagens não aceitam cor¦Impossible d'appliquer une couleur à une image¦이미지에는 색을 설정할 수 없습니다
ハンコ帳が空です¦The stamp book is empty¦印章簿为空¦印章簿為空¦O caderno de carimbos está vazio¦Le carnet de tampons est vide¦도장 모음이 비어 있습니다
ハンコ帳に登録しました（ハンコツールで使えます）¦Added to the stamp book (use it with the Stamp tool)¦已加入印章簿（可用印章工具使用）¦已加入印章簿（可用印章工具使用）¦Adicionado ao caderno (use com a ferramenta Carimbo)¦Ajouté au carnet (utilisable avec l'outil Tampon)¦도장 모음에 등록했습니다 (도장 도구에서 사용 가능)
ハンコ帳の読み込み¦Import stamp book¦导入印章簿¦匯入印章簿¦Importar caderno de carimbos¦Importer le carnet¦도장 모음 불러오기
形式が違います¦Invalid format¦格式不正确¦格式不正確¦Formato inválido¦Format non valide¦형식이 다릅니다
ハンコ帳を初期状態に戻します。登録したハンコは消えます。よろしいですか？¦Reset the stamp book? Your saved stamps will be deleted.¦要将印章簿恢复初始状态吗？已添加的印章将被删除。¦要將印章簿恢復初始狀態嗎？已新增的印章將被刪除。¦Restaurar o caderno de carimbos? Seus carimbos salvos serão excluídos.¦Réinitialiser le carnet ? Vos tampons enregistrés seront supprimés.¦도장 모음을 초기화할까요? 등록한 도장은 삭제됩니다.
このページの書き込みを全消去しました（元に戻す で戻せます）¦All markups on this page removed (Undo to restore)¦已清除本页全部标注（可撤销）¦已清除本頁全部標註（可復原）¦Todas as anotações desta página foram removidas (Desfazer para restaurar)¦Toutes les annotations de cette page ont été supprimées (Annuler pour restaurer)¦이 페이지의 주석을 모두 지웠습니다 (실행 취소로 복원)
コピーする文字が選択されていません（ページ上をドラッグで囲んでください）¦No text selected (drag a box on the page)¦未选择要复制的文字（请在页面上拖动框选）¦未選取要複製的文字（請在頁面上拖曳框選）¦Nenhum texto selecionado (arraste uma caixa na página)¦Aucun texte sélectionné (tracez un cadre sur la page)¦복사할 텍스트가 선택되지 않았습니다 (페이지에서 드래그해 둘러싸세요)
この環境ではボタンからコピーできません。右の欄が選択された状態なので Ctrl+C を押してください¦The button can't copy in this environment. The text on the right is selected — press Ctrl+C¦此环境无法通过按钮复制。右侧文字已选中，请按Ctrl+C¦此環境無法透過按鈕複製。右側文字已選取，請按Ctrl+C¦O botão não consegue copiar neste ambiente. O texto à direita está selecionado — pressione Ctrl+C¦Le bouton ne peut pas copier ici. Le texte à droite est sélectionné : appuyez sur Ctrl+C¦이 환경에서는 버튼으로 복사할 수 없습니다. 오른쪽 내용이 선택되어 있으니 Ctrl+C를 누르세요
このページには文字データがありません（スキャン画像のPDFなど）¦This page has no text data (e.g. a scanned PDF)¦此页面没有文字数据（如扫描的PDF）¦此頁面沒有文字資料（如掃描的PDF）¦Esta página não tem texto (ex.: PDF digitalizado)¦Cette page ne contient pas de texte (ex. PDF numérisé)¦이 페이지에는 텍스트 데이터가 없습니다 (스캔 PDF 등)
※まとめ印刷（2in1/4in1）では付箋は書き出されません¦* Sticky notes are not exported in N-up (2-up/4-up)¦※多页合一（2合1/4合1）时不导出便签¦※多頁合一（2合1/4合1）時不匯出便利貼¦* Notas adesivas não são exportadas em várias por folha¦* Les notes ne sont pas exportées en mode pages par feuille¦※모아 찍기(2-in-1/4-in-1)에서는 메모지가 출력되지 않습니다
※ブラウザに保存できませんでした（容量不足または保存不可の設定）¦* Couldn't save in the browser (storage full or disabled)¦※无法保存到浏览器（容量不足或禁止保存）¦※無法儲存到瀏覽器（容量不足或禁止儲存）¦* Não foi possível salvar no navegador (sem espaço ou desativado)¦* Impossible d'enregistrer dans le navigateur (plein ou désactivé)¦※브라우저에 저장하지 못했습니다 (용량 부족 또는 저장 불가 설정)
ハンコを押しました（ハンコツールで続けて押せます）¦Stamped (keep stamping with the Stamp tool)¦已盖章（可用印章工具继续盖）¦已蓋章（可用印章工具繼續蓋）¦Carimbado (continue com a ferramenta Carimbo)¦Tampon appliqué (continuez avec l'outil Tampon)¦도장을 찍었습니다 (도장 도구로 계속 찍을 수 있음)
印影を登録しました¦Seal image registered¦已添加印鉴¦已新增印鑑¦Carimbo registrado¦Tampon ajouté¦인영을 등록했습니다
付箋に直接入力中（Ctrl+Enter または 外をクリックで確定）¦Typing on the note (Ctrl+Enter or click outside to finish)¦正在便签上输入（按Ctrl+Enter或点击外部完成）¦正在便利貼上輸入（按Ctrl+Enter或點擊外部完成）¦Digitando na nota (Ctrl+Enter ou clique fora para concluir)¦Saisie dans la note (Ctrl+Entrée ou cliquez à l'extérieur)¦메모지에 입력 중 (Ctrl+Enter 또는 바깥 클릭으로 확정)
一覧モード：ドラッグで並べ替え・Ctrl/Shift+クリックで複数選択・ダブルクリックで編集¦Grid mode: drag to reorder, Ctrl/Shift+click to multi-select, double-click to edit¦网格模式：拖动排序，Ctrl/Shift+点击多选，双击编辑¦網格模式：拖曳排序，Ctrl/Shift+點擊多選，雙擊編輯¦Modo grade: arraste para reordenar, Ctrl/Shift+clique para selecionar vários, clique duplo para editar¦Mode grille : glisser pour réordonner, Ctrl/Maj+clic pour sélectionner, double-clic pour éditer¦목록 모드: 드래그로 순서 변경, Ctrl/Shift+클릭으로 여러 개 선택, 더블클릭으로 편집
編集モード：右のページに直接書き込めます¦Edit mode: annotate the page on the right¦编辑模式：可直接在右侧页面上标注¦編輯模式：可直接在右側頁面上標註¦Modo de edição: anote diretamente a página à direita¦Mode édition : annotez directement la page à droite¦편집 모드: 오른쪽 페이지에 직접 주석을 넣을 수 있습니다
書き込みをクリックで選択 → ドラッグで移動・四隅で拡大縮小・Deleteで削除¦Click a markup to select → drag to move, corners to resize, Delete to remove¦点击标注即可选择 → 拖动移动，拖四角缩放，按Delete删除¦點擊標註即可選取 → 拖曳移動，拖四角縮放，按Delete刪除¦Clique numa anotação para selecionar → arraste para mover, cantos para redimensionar, Delete para excluir¦Cliquez sur une annotation → glissez pour déplacer, coins pour redimensionner, Suppr pour effacer¦주석을 클릭해 선택 → 드래그로 이동, 모서리로 크기 조절, Delete로 삭제
ドラッグで範囲を指定¦Drag to draw¦拖动指定范围¦拖曳指定範圍¦Arraste para desenhar¦Faites glisser pour tracer¦드래그로 범위 지정
ドラッグで描く¦Drag to draw¦拖动绘制¦拖曳繪製¦Arraste para desenhar¦Faites glisser pour dessiner¦드래그로 그리기
ドラッグでなぞる¦Drag over text¦拖动涂画¦拖曳描畫¦Arraste sobre o texto¦Glissez sur le texte¦드래그로 덧칠하기
ドラッグで描く（Shiftで直線・45°刻み、Ctrlで直線）¦Drag to draw (Shift: straight line in 45° steps, Ctrl: straight line)¦拖动绘制（Shift：45°直线，Ctrl：直线）¦拖曳繪製（Shift：45°直線，Ctrl：直線）¦Arraste para desenhar (Shift: linha reta em passos de 45°, Ctrl: linha reta)¦Glissez pour dessiner (Maj : ligne droite par 45°, Ctrl : ligne droite)¦드래그로 그리기 (Shift: 45° 단위 직선, Ctrl: 직선)
ドラッグでなぞる（Shiftで直線・45°刻み、Ctrlで直線）¦Drag over text (Shift: straight line in 45° steps, Ctrl: straight line)¦拖动涂画（Shift：45°直线，Ctrl：直线）¦拖曳描畫（Shift：45°直線，Ctrl：直線）¦Arraste sobre o texto (Shift: linha reta em passos de 45°, Ctrl: linha reta)¦Glissez sur le texte (Maj : ligne droite par 45°, Ctrl : ligne droite)¦드래그로 덧칠 (Shift: 45° 단위 직선, Ctrl: 직선)
ドラッグで描く（ゆっくり＝太く、速く＝細く。ペンタブは筆圧対応／Shiftで直線）¦Drag to draw (slow = thick, fast = thin; pen tablets use pressure / Shift: straight line)¦拖动绘制（慢＝粗，快＝细；数位板支持压感／Shift：直线）¦拖曳繪製（慢＝粗，快＝細；繪圖板支援壓感／Shift：直線）¦Arraste para desenhar (devagar = grosso, rápido = fino; mesa digitalizadora usa pressão / Shift: linha reta)¦Glissez pour dessiner (lent = épais, rapide = fin ; tablette : pression / Maj : ligne droite)¦드래그로 그리기 (천천히=굵게, 빠르게=가늘게. 펜 태블릿은 필압 지원 / Shift: 직선)
ドラッグで消す（ペン類は部分的に、それ以外は丸ごと。元のPDFは消えません）¦Drag to erase (pen strokes partially, other items entirely; the original PDF is never erased)¦拖动擦除（笔迹可部分擦除，其他整体删除；原PDF不会被擦除）¦拖曳擦除（筆跡可部分擦除，其他整體刪除；原PDF不會被擦除）¦Arraste para apagar (traços parcialmente, outros itens inteiros; o PDF original nunca é apagado)¦Glissez pour effacer (traits en partie, autres éléments entiers ; le PDF d'origine n'est jamais effacé)¦드래그로 지우기 (펜 선은 부분적으로, 그 외는 통째로. 원본 PDF는 지워지지 않음)
書き込みをクリック＝色を変える／ペン等で囲んだ内側をクリック＝塗りつぶす¦Click a markup = recolor / click inside a closed pen line = fill¦点击标注＝改色／点击笔等围出的内侧＝填充¦點擊標註＝改色／點擊筆等圍出的內側＝填色¦Clique numa anotação = mudar cor / clique dentro de uma linha fechada = preencher¦Cliquez une annotation = recolorer / à l'intérieur d'un tracé fermé = remplir¦주석 클릭 = 색 변경 / 펜 등으로 둘러싼 안쪽 클릭 = 채우기
色を拾いたい所をクリック → 直前のツール（または選んでいた書き込み）にその色をセット。描画中は Alt+クリックでも拾えます¦Click where you want to pick a color → it's set on the previous tool (or selected markup). While drawing, Alt+click also picks¦点击要拾取颜色的位置 → 设置到上一个工具（或所选标注）。绘制时也可Alt+点击拾取¦點擊要擷取顏色的位置 → 設定到上一個工具（或所選標註）。繪製時也可Alt+點擊擷取¦Clique onde quer pegar a cor → ela vai para a ferramenta anterior (ou anotação selecionada). Ao desenhar, Alt+clique também pega¦Cliquez où prélever une couleur → appliquée à l'outil précédent (ou à l'annotation sélectionnée). En dessinant, Alt+clic prélève aussi¦색을 가져올 곳을 클릭 → 직전 도구(또는 선택한 주석)에 그 색을 설정. 그리는 중에는 Alt+클릭으로도 가능
文字を置きたい位置をクリック¦Click where you want the text¦点击要放置文字的位置¦點擊要放置文字的位置¦Clique onde quer o texto¦Cliquez à l'emplacement du texte¦텍스트를 넣을 위치를 클릭
コピーしたい範囲をドラッグで囲む（枠内の文字だけを選択）¦Drag a box around what to copy (only text inside the box is selected)¦拖动框选要复制的范围（只选择框内文字）¦拖曳框選要複製的範圍（只選取框內文字）¦Arraste uma caixa ao redor do que copiar (só o texto dentro é selecionado)¦Tracez un cadre autour du texte à copier (seul le texte à l'intérieur est sélectionné)¦복사할 범위를 드래그로 둘러싸기 (테두리 안의 텍스트만 선택)
クリックで付箋を貼る（ドラッグで大きさを指定）→ そのまま文字を入力¦Click to add a note (drag to set its size) → then type¦点击贴上便签（拖动指定大小）→ 直接输入文字¦點擊貼上便利貼（拖曳指定大小）→ 直接輸入文字¦Clique para adicionar uma nota (arraste para definir o tamanho) → digite¦Cliquez pour ajouter une note (glissez pour la taille) → puis tapez¦클릭해 메모지 붙이기 (드래그로 크기 지정) → 바로 입력
右のハンコ帳から選んで、押したい位置をクリック¦Pick a stamp from the book on the right, then click where to stamp¦从右侧印章簿选择，然后点击要盖章的位置¦從右側印章簿選擇，然後點擊要蓋章的位置¦Escolha um carimbo no caderno à direita e clique onde carimbar¦Choisissez un tampon dans le carnet à droite, puis cliquez¦오른쪽 도장 모음에서 골라 찍을 위치를 클릭
テキスト¦Text¦文本¦文字¦Texto¦Texte¦텍스트
新しいハンコ¦New stamp¦新印章¦新印章¦Novo carimbo¦Nouveau tampon¦새 도장
_加工¦_edited¦_已编辑¦_已編輯¦_editado¦_modifie¦_편집
_作業ファイル¦_workfile¦_工作文件¦_工作檔案¦_trabalho¦_travail¦_작업파일
作業ファイル¦Work file¦工作文件¦工作檔案¦Arquivo de trabalho¦Fichier de travail¦작업 파일
エディター¦Editor¦编辑器¦編輯器¦Editor¦Éditeur¦편집기
見た目¦Skin¦皮肤¦外觀¦Tema¦Thème¦스킨
フォルダ¦Folder¦文件夹¦資料夾¦Pasta¦Dossier¦폴더
フォルダを選ぶ¦Choose folder¦选择文件夹¦選擇資料夾¦Escolher pasta¦Choisir un dossier¦폴더 선택
更新¦Refresh¦刷新¦重新整理¦Atualizar¦Actualiser¦새로 고침
整列¦Arrange¦整理排列¦整齊排列¦Organizar¦Ranger¦정렬
文書¦Document¦文档¦文件¦Documento¦Document¦문서
プレビュー¦Preview¦预览¦預覽¦Visualizar¦Aperçu¦미리 보기
名前変更¦Rename¦重命名¦重新命名¦Renomear¦Renommer¦이름 변경
印刷¦Print¦打印¦列印¦Imprimir¦Imprimer¦인쇄
_削除予定へ¦Set aside to delete¦移到待删除¦移到待刪除¦Separar para excluir¦Mettre de côté à supprimer¦삭제 예정으로
ログ¦Log¦日志¦日誌¦Log¦Journal¦로그
ログコピー¦Copy log¦复制日志¦複製日誌¦Copiar log¦Copier le journal¦로그 복사
このフォルダには PDF・作業ファイル・画像がありません¦This folder has no PDFs, work files or images¦此文件夹中没有PDF、工作文件或图片¦此資料夾中沒有PDF、工作檔案或圖片¦Esta pasta não tem PDFs, arquivos de trabalho ou imagens¦Ce dossier ne contient ni PDF, ni fichier de travail, ni image¦이 폴더에는 PDF・작업 파일・이미지가 없습니다
エクスプローラーからドラッグ＆ドロップで取り込めます¦Drag & drop from Explorer to import¦可从资源管理器拖放导入¦可從檔案總管拖放匯入¦Arraste e solte do Explorer para importar¦Glissez-déposez depuis l'Explorateur pour importer¦탐색기에서 드래그 앤 드롭으로 가져올 수 있습니다
← 前¦← Prev¦← 上一页¦← 上一頁¦← Anterior¦← Préc.¦← 이전
次 →¦Next →¦下一页 →¦下一頁 →¦Próxima →¦Suiv. →¦다음 →
ダブルクリック：開く ／ 重ねる：結合 ／ Space・Ctrl+Shift：プレビュー ／ F2：名前変更 ／ Ctrl+C・V：複製 ／ Ctrl+Z：元に戻す¦Double-click: open / Overlap: merge / Space・Ctrl+Shift: preview / F2: rename / Ctrl+C・V: duplicate / Ctrl+Z: undo¦双击：打开 ／ 重叠：合并 ／ Space・Ctrl+Shift：预览 ／ F2：重命名 ／ Ctrl+C・V：复制 ／ Ctrl+Z：撤销¦雙擊：開啟 ／ 重疊：合併 ／ Space・Ctrl+Shift：預覽 ／ F2：重新命名 ／ Ctrl+C・V：複製 ／ Ctrl+Z：復原¦Clique duplo: abrir / Sobrepor: unir / Space・Ctrl+Shift: visualizar / F2: renomear / Ctrl+C・V: duplicar / Ctrl+Z: desfazer¦Double-clic : ouvrir / Superposer : fusionner / Space・Ctrl+Shift : aperçu / F2 : renommer / Ctrl+C・V : dupliquer / Ctrl+Z : annuler¦더블클릭: 열기 / 겹치기: 결합 / Space・Ctrl+Shift: 미리 보기 / F2: 이름 변경 / Ctrl+C・V: 복제 / Ctrl+Z: 실행 취소
前回のフォルダを開きます¦Open the last folder¦打开上次的文件夹¦開啟上次的資料夾¦Abrir a última pasta¦Ouvrir le dernier dossier¦지난번 폴더를 엽니다
フォルダを開きます¦Open folder¦打开文件夹¦開啟資料夾¦Abrir pasta¦Ouvrir le dossier¦폴더를 엽니다
クリックすると開きます（ブラウザの決まりで、起動時に1回だけ確認が出ることがあります）¦Click to open (the browser may ask for permission once at startup)¦点击即可打开（按浏览器规则，启动时可能会确认一次）¦點擊即可開啟（依瀏覽器規定，啟動時可能會確認一次）¦Clique para abrir (o navegador pode pedir permissão uma vez ao iniciar)¦Cliquez pour ouvrir (le navigateur peut demander une autorisation une fois au démarrage)¦클릭하면 열립니다 (브라우저 규칙상 시작 시 한 번 확인이 나올 수 있습니다)
クリックすると開きます¦Click to open¦点击即可打开¦點擊即可開啟¦Clique para abrir¦Cliquez pour ouvrir¦클릭하면 열립니다
結合¦Merge¦合并¦合併¦Unir¦Fusionner¦결합
この順番で1つにまとめます（↑↓で並べ替え）¦Combine into one in this order (↑↓ to reorder)¦按此顺序合并为一个（↑↓调整顺序）¦依此順序合併為一個（↑↓調整順序）¦Juntar em um, nesta ordem (↑↓ para reordenar)¦Regrouper en un seul, dans cet ordre (↑↓ pour réordonner)¦이 순서로 하나로 합칩니다 (↑↓로 순서 변경)
画像は PDF のページに変換してから結合します¦Images are converted to PDF pages before merging¦图片会先转换为PDF页面再合并¦圖片會先轉換為PDF頁面再合併¦As imagens são convertidas em páginas PDF antes de unir¦Les images sont converties en pages PDF avant la fusion¦이미지는 PDF 페이지로 변환한 뒤 결합합니다
作業ファイルを含むので、結果は作業ファイル（.frontpdf）になります。書き込み・付箋などはそのまま残り、エディターで続きから編集できます¦Because work files are included, the result is a work file (.frontpdf). Markups, notes etc. are kept, and you can continue editing in the editor¦由于包含工作文件，结果将是工作文件（.frontpdf）。标注、便签等会保留，可在编辑器中继续编辑¦由於包含工作檔案，結果將是工作檔案（.frontpdf）。標註、便籤等會保留，可在編輯器中繼續編輯¦Como há arquivos de trabalho, o resultado será um arquivo de trabalho (.frontpdf). Anotações, notas etc. são mantidas e você pode continuar editando no editor¦Comme des fichiers de travail sont inclus, le résultat sera un fichier de travail (.frontpdf). Annotations, notes, etc. sont conservées et vous pouvez continuer dans l'éditeur¦작업 파일이 포함되어 있으므로 결과는 작업 파일(.frontpdf)이 됩니다. 주석・메모 등은 그대로 남고 편집기에서 이어서 편집할 수 있습니다
新しいファイル名¦New file name¦新文件名¦新檔名¦Novo nome do arquivo¦Nouveau nom de fichier¦새 파일 이름
元のファイルを「_削除予定」へ移す¦Move the original files to "_削除予定" (to-delete folder)¦将原文件移到"_削除予定"（待删除文件夹）¦將原檔案移到「_削除予定」（待刪除資料夾）¦Mover os originais para "_削除予定" (pasta de exclusão)¦Déplacer les originaux vers « _削除予定 » (dossier à supprimer)¦원본 파일을 '_削除予定'(삭제 예정 폴더)으로 이동
結合しても、デスクの［元に戻す］（Ctrl+Z）で結合前に戻せます¦You can undo the merge with [Undo] (Ctrl+Z) on the desk¦合并后也可用桌面的［撤销］（Ctrl+Z）恢复¦合併後也可用桌面的［復原］（Ctrl+Z）還原¦Você pode desfazer a união com [Desfazer] (Ctrl+Z) na mesa¦Vous pouvez annuler la fusion avec [Annuler] (Ctrl+Z) sur le bureau¦결합해도 데스크의 [실행 취소](Ctrl+Z)로 되돌릴 수 있습니다
結合する¦Merge¦合并¦合併¦Unir¦Fusionner¦결합
ページごとにばらす¦Split into pages¦按页拆分¦按頁拆分¦Separar por página¦Séparer par page¦페이지별로 나누기
同じフォルダに保存¦Save in the same folder¦保存到同一文件夹¦儲存到同一資料夾¦Salvar na mesma pasta¦Enregistrer dans le même dossier¦같은 폴더에 저장
新しいフォルダにまとめる¦Put them in a new folder¦放入新文件夹¦放入新資料夾¦Colocar numa nova pasta¦Les mettre dans un nouveau dossier¦새 폴더에 모으기
ばらしても、デスクの［元に戻す］（Ctrl+Z）で元に戻せます¦You can undo the split with [Undo] (Ctrl+Z) on the desk¦拆分后也可用桌面的［撤销］（Ctrl+Z）恢复¦拆分後也可用桌面的［復原］（Ctrl+Z）還原¦Você pode desfazer com [Desfazer] (Ctrl+Z) na mesa¦Vous pouvez annuler avec [Annuler] (Ctrl+Z) sur le bureau¦나눠도 데스크의 [실행 취소](Ctrl+Z)로 되돌릴 수 있습니다
ばらす¦Split¦拆分¦拆分¦Separar¦Séparer¦나누기
デスクへ¦Desk¦桌面¦桌面¦Mesa¦Bureau¦데스크
デスクを表示¦Show desk¦显示桌面¦顯示桌面¦Mostrar mesa¦Afficher le bureau¦데스크 표시
デスク¦Desk¦桌面¦桌面¦Mesa¦Bureau¦데스크
PDF保存¦Save PDF¦保存PDF¦儲存PDF¦Salvar PDF¦Enregistrer PDF¦PDF 저장
作業ファイル保存¦Save work file¦保存工作文件¦儲存工作檔案¦Salvar arq. de trabalho¦Enreg. fichier de travail¦작업 파일 저장
別名で保存¦Save as¦另存为¦另存新檔¦Salvar como¦Enregistrer sous¦다른 이름으로 저장
形式¦Format¦格式¦格式¦Formato¦Format¦형식
作業ファイル（.frontpdf：続きから編集できる）¦Work file (.frontpdf: continue editing later)¦工作文件（.frontpdf：可继续编辑）¦工作檔案（.frontpdf：可繼續編輯）¦Arquivo de trabalho (.frontpdf: continuar editando depois)¦Fichier de travail (.frontpdf : reprendre l'édition plus tard)¦작업 파일(.frontpdf: 이어서 편집 가능)
保存前の確認（黒塗り）¦Check before saving (black-out)¦保存前确认（涂黑）¦儲存前確認（塗黑）¦Verificação antes de salvar (tarjas)¦Vérification avant l'enregistrement (masquage)¦저장 전 확인 (검게 칠하기)
塗った部分を画像にして保存（推奨・下の文字は消える）¦Save masked parts as images (recommended; text underneath is removed)¦将涂抹部分转为图像保存（推荐・下方文字会被删除）¦將塗抹部分轉為影像儲存（推薦・下方文字會被刪除）¦Salvar as partes tarjadas como imagem (recomendado; o texto embaixo é removido)¦Enregistrer les zones masquées en image (recommandé ; le texte dessous est supprimé)¦칠한 부분을 이미지로 저장 (권장・아래 텍스트는 지워짐)
元のデータのまま保存（下の文字は残る）¦Save the original data as is (text underneath remains)¦按原数据保存（下方文字会保留）¦按原資料儲存（下方文字會保留）¦Salvar os dados originais (o texto embaixo permanece)¦Enregistrer les données d'origine (le texte dessous reste)¦원본 데이터 그대로 저장 (아래 텍스트는 남음)
エディター（PDF に書き込む画面）を別ウインドウで開く¦Open the editor (where you mark up PDFs) in a new window¦在新窗口打开编辑器（在PDF上书写的界面）¦在新視窗開啟編輯器（在PDF上書寫的畫面）¦Abrir o editor (onde você anota PDFs) em nova janela¦Ouvrir l'éditeur (pour annoter les PDF) dans une nouvelle fenêtre¦편집기(PDF에 쓰는 화면)를 새 창으로 열기
デスクに並べるいちばん上のフォルダを選ぶ（Box のフォルダも可）¦Choose the top folder to show on the desk (Box folders work too)¦选择要在桌面上显示的顶层文件夹（也可选Box文件夹）¦選擇要在桌面上顯示的最上層資料夾（也可選Box資料夾）¦Escolha a pasta superior a exibir na mesa (pastas do Box também)¦Choisissez le dossier racine à afficher sur le bureau (dossiers Box acceptés)¦데스크에 표시할 최상위 폴더 선택 (Box 폴더도 가능)
一覧を読み直す¦Reload the list¦重新读取列表¦重新讀取清單¦Recarregar a lista¦Recharger la liste¦목록 다시 읽기
ファイル名で絞り込み¦Filter by file name¦按文件名筛选¦依檔名篩選¦Filtrar por nome¦Filtrer par nom de fichier¦파일 이름으로 필터
名前順にきれいに並べ直す¦Rearrange neatly by name¦按名称重新整齐排列¦依名稱重新整齊排列¦Reorganizar por nome¦Réorganiser proprement par nom¦이름순으로 깔끔하게 다시 정렬
別ウインドウのエディターで開く（ダブルクリックでも開けます）¦Open in the editor in a new window (double-click also works)¦在新窗口的编辑器中打开（也可双击）¦在新視窗的編輯器中開啟（也可雙擊）¦Abrir no editor em nova janela (clique duplo também)¦Ouvrir dans l'éditeur dans une nouvelle fenêtre (double-clic aussi)¦새 창 편집기로 열기 (더블클릭으로도 열림)
開かずに大きく確認（スペースキー）¦View large without opening (Space)¦不打开直接放大查看（空格键）¦不開啟直接放大查看（空白鍵）¦Ver ampliado sem abrir (Espaço)¦Voir en grand sans ouvrir (Espace)¦열지 않고 크게 확인 (스페이스)
名前を変える（F2）¦Rename (F2)¦重命名（F2）¦重新命名（F2）¦Renomear (F2)¦Renommer (F2)¦이름 변경 (F2)
選んだ PDF・画像を印刷（Ctrl+P）¦Print the selected PDFs and images (Ctrl+P)¦打印所选PDF和图片（Ctrl+P）¦列印所選PDF和圖片（Ctrl+P）¦Imprimir PDFs e imagens selecionados (Ctrl+P)¦Imprimer les PDF et images sélectionnés (Ctrl+P)¦선택한 PDF・이미지 인쇄 (Ctrl+P)
「_削除予定」フォルダへ移す（Delete）¦Move to the "_削除予定" (to-delete folder) folder (Delete)¦移到"_削除予定"（待删除文件夹）文件夹（Delete）¦移到「_削除予定」（待刪除資料夾）資料夾（Delete）¦Mover para a pasta "_削除予定" (pasta de exclusão) (Delete)¦Déplacer vers le dossier « _削除予定 » (dossier à supprimer) (Suppr)¦'_削除予定'(삭제 예정 폴더) 폴더로 이동 (Delete)
元に戻す（Ctrl+Z）何回でも戻せます¦Undo (Ctrl+Z) — as many times as you like¦撤销（Ctrl+Z）可多次撤销¦復原（Ctrl+Z）可多次復原¦Desfazer (Ctrl+Z) — quantas vezes quiser¦Annuler (Ctrl+Z) — autant de fois que nécessaire¦실행 취소 (Ctrl+Z) 몇 번이든 가능
やり直し（Ctrl+Y）¦Redo (Ctrl+Y)¦重做（Ctrl+Y）¦重做（Ctrl+Y）¦Refazer (Ctrl+Y)¦Rétablir (Ctrl+Y)¦다시 실행 (Ctrl+Y)
前のページ（←）¦Previous page (←)¦上一页（←）¦上一頁（←）¦Página anterior (←)¦Page précédente (←)¦이전 페이지 (←)
次のページ（→）¦Next page (→)¦下一页（→）¦下一頁（→）¦Próxima página (→)¦Page suivante (→)¦다음 페이지 (→)
エディターで開く（Enter）¦Open in the editor (Enter)¦在编辑器中打开（Enter）¦在編輯器中開啟（Enter）¦Abrir no editor (Enter)¦Ouvrir dans l'éditeur (Entrée)¦편집기로 열기 (Enter)
閉じる（Esc）¦Close (Esc)¦关闭（Esc）¦關閉（Esc）¦Fechar (Esc)¦Fermer (Échap)¦닫기 (Esc)
デスク（フォルダの書類を並べる画面）に切り替え¦Switch to the desk (shows a folder's documents)¦切换到桌面（排列文件夹文档的界面）¦切換到桌面（排列資料夾文件的畫面）¦Mudar para a mesa (mostra os documentos da pasta)¦Passer au bureau (affiche les documents du dossier)¦데스크(폴더의 문서를 늘어놓는 화면)로 전환
PDF で保存。デスクから開いた PDF はそのまま書き換えます（前の版は「_削除予定」に残ります）¦Save as PDF. A PDF opened from the desk is overwritten (the previous version is kept in "_削除予定")¦保存为PDF。从桌面打开的PDF会直接覆盖（旧版本保留在"_削除予定"）¦儲存為PDF。從桌面開啟的PDF會直接覆寫（舊版本保留在「_削除予定」）¦Salvar como PDF. Um PDF aberto pela mesa é sobrescrito (a versão anterior fica em "_削除予定")¦Enregistrer en PDF. Un PDF ouvert depuis le bureau est écrasé (l'ancienne version reste dans « _削除予定 »)¦PDF로 저장. 데스크에서 연 PDF는 그대로 덮어씁니다 (이전 버전은 '_削除予定'에 남음)
作業ファイル(.frontpdf)で保存。作業ファイルを開いているときは上書き。あとで続きから編集できます¦Save as a work file (.frontpdf). Overwrites when a work file is open. You can continue editing later¦保存为工作文件(.frontpdf)。打开工作文件时会覆盖。之后可继续编辑¦儲存為工作檔案(.frontpdf)。開啟工作檔案時會覆寫。之後可繼續編輯¦Salvar como arquivo de trabalho (.frontpdf). Sobrescreve se um estiver aberto. Dá para continuar depois¦Enregistrer en fichier de travail (.frontpdf). Écrase s'il est déjà ouvert. Vous pourrez reprendre plus tard¦작업 파일(.frontpdf)로 저장. 작업 파일을 열고 있으면 덮어씀. 나중에 이어서 편집 가능
名前と形式（PDF / 作業ファイル）を選んで保存。分割・A4揃え・まとめ印刷も選べます¦Choose a name and format (PDF / work file) to save. Splitting, A4 fit and n-up are also available¦选择名称和格式（PDF / 工作文件）保存。也可选择拆分、A4统一、多页合印¦選擇名稱和格式（PDF / 工作檔案）儲存。也可選擇拆分、A4統一、多頁合印¦Escolha nome e formato (PDF / arquivo de trabalho). Também há divisão, ajuste A4 e várias por folha¦Choisissez nom et format (PDF / fichier de travail). Découpage, format A4 et plusieurs pages par feuille disponibles¦이름과 형식(PDF / 작업 파일)을 골라 저장. 분할・A4 맞춤・모아 찍기도 선택 가능
印刷 (Ctrl+P)¦Print (Ctrl+P)¦打印 (Ctrl+P)¦列印 (Ctrl+P)¦Imprimir (Ctrl+P)¦Imprimer (Ctrl+P)¦인쇄 (Ctrl+P)
印刷（Ctrl+P）¦Print (Ctrl+P)¦打印（Ctrl+P）¦列印（Ctrl+P）¦Imprimir (Ctrl+P)¦Imprimer (Ctrl+P)¦인쇄 (Ctrl+P)
ページを PNG 画像で保存¦Save pages as PNG images¦将页面保存为PNG图片¦將頁面儲存為PNG圖片¦Salvar páginas como imagens PNG¦Enregistrer les pages en images PNG¦페이지를 PNG 이미지로 저장
読み込み中…¦Loading…¦加载中…¦載入中…¦Carregando…¦Chargement…¦불러오는 중…
表示できません¦Cannot display¦无法显示¦無法顯示¦Não é possível exibir¦Impossible d'afficher¦표시할 수 없습니다
このブラウザではフォルダを開けません。Microsoft Edge か Google Chrome をお使いください。¦This browser cannot open folders. Please use Microsoft Edge or Google Chrome.¦此浏览器无法打开文件夹。请使用 Microsoft Edge 或 Google Chrome。¦此瀏覽器無法開啟資料夾。請使用 Microsoft Edge 或 Google Chrome。¦Este navegador não abre pastas. Use o Microsoft Edge ou o Google Chrome.¦Ce navigateur ne peut pas ouvrir de dossiers. Utilisez Microsoft Edge ou Google Chrome.¦이 브라우저에서는 폴더를 열 수 없습니다. Microsoft Edge 또는 Google Chrome을 사용하세요.
フォルダへのアクセスが許可されませんでした¦Access to the folder was not allowed¦未获得文件夹访问权限¦未取得資料夾存取權限¦O acesso à pasta não foi permitido¦L'accès au dossier n'a pas été autorisé¦폴더 접근이 허용되지 않았습니다
やり直す操作がありません¦Nothing to redo¦没有可重做的操作¦沒有可重做的操作¦Nada para refazer¦Rien à rétablir¦다시 실행할 작업이 없습니다
新しい名前¦New name¦新名称¦新名稱¦Novo nome¦Nouveau nom¦새 이름
次の文字は使えません： \ / : * ? " < > |¦These characters cannot be used: \ / : * ? " < > |¦不能使用以下字符： \ / : * ? " < > |¦不能使用以下字元： \ / : * ? " < > |¦Estes caracteres não podem ser usados: \ / : * ? " < > |¦Ces caractères sont interdits : \ / : * ? " < > |¦다음 문자는 사용할 수 없습니다: \ / : * ? " < > |
同じ名前のファイルがあります。¦A file with the same name already exists.¦已有同名文件。¦已有同名檔案。¦Já existe um arquivo com esse nome.¦Un fichier du même nom existe déjà.¦같은 이름의 파일이 있습니다.
名前変更できません¦Cannot rename¦无法重命名¦無法重新命名¦Não foi possível renomear¦Impossible de renommer¦이름을 바꿀 수 없습니다
移動できません¦Cannot move¦无法移动¦無法移動¦Não foi possível mover¦Impossible de déplacer¦이동할 수 없습니다
_削除予定へ移せません¦Cannot move to "_削除予定"¦无法移到"_削除予定"¦無法移到「_削除予定」¦Não foi possível mover para "_削除予定"¦Impossible de déplacer vers « _削除予定 »¦'_削除予定'(으)로 옮길 수 없습니다
貼り付けできません¦Cannot paste¦无法粘贴¦無法貼上¦Não foi possível colar¦Impossible de coller¦붙여넣을 수 없습니다
取り込めません¦Cannot import¦无法导入¦無法匯入¦Não foi possível importar¦Impossible d'importer¦가져올 수 없습니다
結合できません¦Cannot merge¦无法合并¦無法合併¦Não foi possível unir¦Impossible de fusionner¦결합할 수 없습니다
ばらせません¦Cannot split¦无法拆分¦無法拆分¦Não foi possível separar¦Impossible de séparer¦나눌 수 없습니다
途中まで作ったファイルは片付けました。もう一度「ばらす」を試してください¦The partly created files were cleaned up. Please try Split again¦已清理中途生成的文件。请再次尝试拆分¦已清理中途產生的檔案。請再次嘗試拆分¦Os arquivos criados pela metade foram removidos. Tente separar de novo¦Les fichiers créés en partie ont été supprimés. Réessayez de séparer¦도중까지 만든 파일을 정리했습니다. 다시 나누기를 시도하세요
PDF か作業ファイルを選んでください（画像はばらせません）。¦Please select PDFs or work files (images cannot be split).¦请选择PDF或工作文件（图片无法拆分）。¦請選擇PDF或工作檔案（圖片無法拆分）。¦Selecione PDFs ou arquivos de trabalho (imagens não podem ser separadas).¦Sélectionnez des PDF ou des fichiers de travail (les images ne peuvent pas être séparées).¦PDF 또는 작업 파일을 선택하세요(이미지는 나눌 수 없습니다).
PDF を選んでください（作業ファイル・画像はばらせません）。¦Please select PDFs (work files and images cannot be split).¦请选择PDF（工作文件和图片无法拆分）。¦請選擇PDF（工作檔案和圖片無法拆分）。¦Selecione PDFs (arquivos de trabalho e imagens não podem ser separados).¦Sélectionnez des PDF (les fichiers de travail et images ne peuvent pas être séparés).¦PDF를 선택하세요 (작업 파일・이미지는 나눌 수 없습니다).
ページ別¦pages¦按页¦按頁¦paginas¦pages¦페이지별
_ページ別¦_pages¦_按页¦_按頁¦_paginas¦_pages¦_페이지별
ページごとに分けています...¦Splitting into pages...¦正在按页拆分...¦正在按頁拆分...¦Separando por página...¦Séparation par page...¦페이지별로 나누는 중...
新しいフォルダの名前¦Name of the new folder¦新文件夹名称¦新資料夾名稱¦Nome da nova pasta¦Nom du nouveau dossier¦새 폴더 이름
新しいフォルダ¦New folder¦新建文件夹¦新資料夾¦Nova pasta¦Nouveau dossier¦새 폴더
同じ名前のフォルダがあります。¦A folder with the same name already exists.¦已有同名文件夹。¦已有同名資料夾。¦Já existe uma pasta com esse nome.¦Un dossier du même nom existe déjà.¦같은 이름의 폴더가 있습니다.
フォルダを作れません¦Cannot create the folder¦无法创建文件夹¦無法建立資料夾¦Não foi possível criar a pasta¦Impossible de créer le dossier¦폴더를 만들 수 없습니다
印刷する PDF・画像を選んでください（作業ファイルはエディターで開いて印刷してください）。¦Select PDFs or images to print (open work files in the editor to print them).¦请选择要打印的PDF或图片（工作文件请在编辑器中打开后打印）。¦請選擇要列印的PDF或圖片（工作檔案請在編輯器中開啟後列印）。¦Selecione PDFs ou imagens para imprimir (abra arquivos de trabalho no editor para imprimir).¦Sélectionnez des PDF ou images à imprimer (ouvrez les fichiers de travail dans l'éditeur pour les imprimer).¦인쇄할 PDF・이미지를 선택하세요 (작업 파일은 편집기에서 열어 인쇄하세요).
印刷の準備中...¦Preparing to print...¦正在准备打印...¦正在準備列印...¦Preparando impressão...¦Préparation de l'impression...¦인쇄 준비 중...
印刷できません¦Cannot print¦无法打印¦無法列印¦Não foi possível imprimir¦Impossible d'imprimer¦인쇄할 수 없습니다
印刷するページがありません。¦There are no pages to print.¦没有要打印的页面。¦沒有要列印的頁面。¦Não há páginas para imprimir.¦Aucune page à imprimer.¦인쇄할 페이지가 없습니다.
このフォルダを開く¦Open this folder¦打开此文件夹¦開啟此資料夾¦Abrir esta pasta¦Ouvrir ce dossier¦이 폴더 열기
ここに貼り付け¦Paste here¦粘贴到此处¦貼上到此處¦Colar aqui¦Coller ici¦여기에 붙여넣기
この中に新しいフォルダ¦New folder inside¦在此新建文件夹¦在此新增資料夾¦Nova pasta aqui dentro¦Nouveau dossier à l'intérieur¦이 안에 새 폴더
名前の変更¦Rename¦重命名¦重新命名¦Renomear¦Renommer¦이름 변경
貼り付け¦Paste¦粘贴¦貼上¦Colar¦Coller¦붙여넣기
複製（このフォルダに）¦Duplicate (in this folder)¦复制（到此文件夹）¦複製（到此資料夾）¦Duplicar (nesta pasta)¦Dupliquer (dans ce dossier)¦복제 (이 폴더에)
結合（2件以上を選んでください）¦Merge (select 2 or more)¦合并（请选择2个以上）¦合併（請選擇2個以上）¦Unir (selecione 2 ou mais)¦Fusionner (sélectionnez-en 2 ou plus)¦결합 (2개 이상 선택)
すべて選択¦Select all¦全选¦全選¦Selecionar tudo¦Tout sélectionner¦모두 선택
名前順に整列¦Arrange by name¦按名称排列¦依名稱排列¦Organizar por nome¦Ranger par nom¦이름순 정렬
ポップアップがブロックされました。¦The pop-up was blocked.¦弹出窗口被阻止了。¦彈出視窗被封鎖了。¦O pop-up foi bloqueado.¦La fenêtre pop-up a été bloquée.¦팝업이 차단되었습니다.
別ウインドウ¦New window¦新窗口¦新視窗¦Nova janela¦Nouvelle fenêtre¦새 창
別ウインドウで開けません¦Cannot open in a new window¦无法在新窗口打开¦無法在新視窗開啟¦Não foi possível abrir em nova janela¦Impossible d'ouvrir dans une nouvelle fenêtre¦새 창으로 열 수 없습니다
開けません¦Cannot open¦无法打开¦無法開啟¦Não foi possível abrir¦Impossible d'ouvrir¦열 수 없습니다
エディターで編集中の内容が保存されていません。閉じて別の文書を開きますか？¦Your edits in the editor are not saved. Close them and open another document?¦编辑器中的内容尚未保存。要关闭并打开其他文档吗？¦編輯器中的內容尚未儲存。要關閉並開啟其他文件嗎？¦As edições no editor não foram salvas. Fechar e abrir outro documento?¦Vos modifications dans l'éditeur ne sont pas enregistrées. Fermer et ouvrir un autre document ?¦편집기에서 편집 중인 내용이 저장되지 않았습니다. 닫고 다른 문서를 열까요?
作業ファイルを表示できません¦Cannot display the work file¦无法显示工作文件¦無法顯示工作檔案¦Não é possível exibir o arquivo de trabalho¦Impossible d'afficher le fichier de travail¦작업 파일을 표시할 수 없습니다
名前順に並べ直しました¦Rearranged by name¦已按名称重新排列¦已依名稱重新排列¦Reorganizado por nome¦Réorganisé par nom¦이름순으로 다시 정렬했습니다
前回のフォルダを開けませんでした。もう一度選んでください¦Could not open the last folder. Please choose it again¦无法打开上次的文件夹，请重新选择¦無法開啟上次的資料夾，請重新選擇¦Não foi possível abrir a última pasta. Escolha de novo¦Impossible d'ouvrir le dernier dossier. Choisissez-le à nouveau¦지난번 폴더를 열 수 없었습니다. 다시 선택하세요
フォルダを開けません¦Cannot open the folder¦无法打开文件夹¦無法開啟資料夾¦Não foi possível abrir a pasta¦Impossible d'ouvrir le dossier¦폴더를 열 수 없습니다
結合しています...¦Merging...¦正在合并...¦正在合併...¦Unindo...¦Fusion...¦결합하는 중...
このブラウザではデスクを使えません（Microsoft Edge か Google Chrome をお使いください）。［エディター］から PDF の編集はできます。¦The desk is not available in this browser (please use Microsoft Edge or Google Chrome). You can still edit PDFs with [Editor].¦此浏览器无法使用桌面（请使用 Microsoft Edge 或 Google Chrome）。可通过［编辑器］编辑PDF。¦此瀏覽器無法使用桌面（請使用 Microsoft Edge 或 Google Chrome）。可透過［編輯器］編輯PDF。¦A mesa não funciona neste navegador (use o Microsoft Edge ou o Google Chrome). Você ainda pode editar PDFs com [Editor].¦Le bureau n'est pas disponible dans ce navigateur (utilisez Microsoft Edge ou Google Chrome). Vous pouvez quand même éditer des PDF avec [Éditeur].¦이 브라우저에서는 데스크를 사용할 수 없습니다 (Microsoft Edge 또는 Google Chrome을 사용하세요). [편집기]에서 PDF 편집은 가능합니다.
［フォルダを選ぶ］で、書類のあるフォルダ（Box のフォルダも可）を選んでください。その下のフォルダがここに並びます。¦Use [Choose folder] to pick the folder with your documents (Box folders work too). Its subfolders appear here.¦请用［选择文件夹］选择存放文档的文件夹（也可选Box文件夹）。其下的文件夹会显示在这里。¦請用［選擇資料夾］選擇存放文件的資料夾（也可選Box資料夾）。其下的資料夾會顯示在這裡。¦Use [Escolher pasta] para selecionar a pasta dos documentos (pastas do Box também). As subpastas aparecem aqui.¦Utilisez [Choisir un dossier] pour sélectionner le dossier de vos documents (dossiers Box acceptés). Ses sous-dossiers apparaissent ici.¦[폴더 선택]으로 문서가 있는 폴더(Box 폴더도 가능)를 고르세요. 그 아래 폴더가 여기에 표시됩니다.
フォルダを選んでください¦Please choose a folder¦请选择文件夹¦請選擇資料夾¦Escolha uma pasta¦Choisissez un dossier¦폴더를 선택하세요
Front PDF ― デスク¦Front PDF ― Desk¦Front PDF ― 桌面¦Front PDF ― 桌面¦Front PDF ― Mesa¦Front PDF ― Bureau¦Front PDF ― 데스크
Front PDF デスク¦Front PDF Desk¦Front PDF 桌面¦Front PDF 桌面¦Front PDF Mesa¦Front PDF Bureau¦Front PDF 데스크
フォルダの PDF・作業ファイル・画像をサムネイルで並べて、整理・確認・編集できます¦Lay out a folder's PDFs, work files and images as thumbnails to organize, check and edit them¦将文件夹中的PDF、工作文件和图片以缩略图排列，便于整理、查看和编辑¦將資料夾中的PDF、工作檔案和圖片以縮圖排列，方便整理、檢視和編輯¦Organize, confira e edite os PDFs, arquivos de trabalho e imagens de uma pasta em miniaturas¦Disposez en vignettes les PDF, fichiers de travail et images d'un dossier pour les ranger, vérifier et modifier¦폴더의 PDF・작업 파일・이미지를 썸네일로 늘어놓고 정리・확인・편집할 수 있습니다
上へ¦Up¦上移¦上移¦Para cima¦Monter¦위로
下へ¦Down¦下移¦下移¦Para baixo¦Descendre¦아래로
動作ログを表示（不具合の報告用）¦Show the activity log (for bug reports)¦显示操作日志（用于报告问题）¦顯示操作日誌（用於回報問題）¦Mostrar o log de atividade (para relatar problemas)¦Afficher le journal d'activité (pour signaler un problème)¦동작 로그 표시 (문제 보고용)
動作ログをコピー（不具合の報告に貼り付けてください）¦Copy the activity log (paste it into your bug report)¦复制操作日志（请粘贴到问题报告中）¦複製操作日誌（請貼到問題回報中）¦Copiar o log de atividade (cole no relato do problema)¦Copier le journal d'activité (collez-le dans votre signalement)¦동작 로그 복사 (문제 보고에 붙여넣으세요)
ログをコピーしました。不具合の報告に貼り付けてください¦Log copied. Please paste it into your bug report¦已复制日志。请粘贴到问题报告中¦已複製日誌。請貼到問題回報中¦Log copiado. Cole-o no relato do problema¦Journal copié. Collez-le dans votre signalement¦로그를 복사했습니다. 문제 보고에 붙여넣으세요
空にする（完全に削除）¦Empty (delete permanently)¦清空（永久删除）¦清空（永久刪除）¦Esvaziar (excluir definitivamente)¦Vider (supprimer définitivement)¦비우기 (완전히 삭제)
空にする¦Empty¦清空¦清空¦Esvaziar¦Vider¦비우기
「_削除予定」フォルダは空です。¦The "_削除予定" folder is empty.¦"_削除予定"文件夹是空的。¦「_削除予定」資料夾是空的。¦A pasta "_削除予定" está vazia.¦Le dossier « _削除予定 » est vide.¦'_削除予定' 폴더는 비어 있습니다.
削除しています...¦Deleting...¦正在删除...¦正在刪除...¦Excluindo...¦Suppression...¦삭제하는 중...
「_削除予定」フォルダについて¦About the "_削除予定" folder¦关于"_削除予定"文件夹¦關於「_削除予定」資料夾¦Sobre a pasta "_削除予定"¦À propos du dossier « _削除予定 »¦'_削除予定' 폴더에 대해
このフォルダの中身は、左の一覧でこのフォルダを右クリックして［空にする］で削除してください。¦To delete the contents of this folder, right-click it in the list on the left and choose [Empty].¦要删除此文件夹的内容，请在左侧列表中右键单击此文件夹并选择［清空］。¦要刪除此資料夾的內容，請在左側清單中右鍵點擊此資料夾並選擇［清空］。¦Para excluir o conteúdo desta pasta, clique com o botão direito nela na lista à esquerda e escolha [Esvaziar].¦Pour supprimer le contenu de ce dossier, faites un clic droit dessus dans la liste de gauche et choisissez [Vider].¦이 폴더의 내용은 왼쪽 목록에서 이 폴더를 오른쪽 클릭하고 [비우기]로 삭제하세요.
"""
# dynamic patterns: regex ¦ en ¦ zhCN ¦ zhTW ¦ pt ¦ fr ¦ ko   ($1.. = groups; Japanese groups get translated if known)
PAT=r"""
^「(.+)」の中の (\d+) 件を完全に削除します。\nWindows や Mac のごみ箱には入らず、元に戻せません。\n（デスクの［元に戻す］の履歴もリセットされます）$¦Permanently delete $2 item(s) in "$1"?\nThey do not go to the Windows or Mac trash and cannot be restored.\n(The desk's [Undo] history is also reset)¦将永久删除"$1"中的 $2 项。\n不会进入 Windows 或 Mac 的回收站，无法恢复。\n（桌面的［撤销］记录也会被清除）¦將永久刪除「$1」中的 $2 項。\n不會進入 Windows 或 Mac 的垃圾桶，無法還原。\n（桌面的［復原］記錄也會被清除）¦Excluir definitivamente $2 item(s) em "$1"?\nEles não vão para a lixeira do Windows ou do Mac e não podem ser recuperados.\n(O histórico de [Desfazer] da mesa também é apagado)¦Supprimer définitivement $2 élément(s) dans « $1 » ?\nIls ne vont pas dans la corbeille de Windows ou du Mac et ne peuvent pas être restaurés.\n(L'historique [Annuler] du bureau est aussi réinitialisé)¦'$1' 안의 $2건을 완전히 삭제합니다.\nWindows나 Mac의 휴지통에 들어가지 않으며 되돌릴 수 없습니다.\n(데스크의 [실행 취소] 기록도 초기화됩니다)
^(\d+) 件を完全に削除しました$¦Permanently deleted $1 item(s)¦已永久删除 $1 项¦已永久刪除 $1 項¦$1 item(s) excluído(s) definitivamente¦$1 élément(s) supprimé(s) définitivement¦$1건을 완전히 삭제했습니다
^(\d+) 件を完全に削除しました（(\d+) 件は削除できませんでした）$¦Permanently deleted $1 item(s) ($2 could not be deleted)¦已永久删除 $1 项（$2 项无法删除）¦已永久刪除 $1 項（$2 項無法刪除）¦$1 item(s) excluído(s) definitivamente ($2 não puderam ser excluídos)¦$1 élément(s) supprimé(s) définitivement ($2 n'ont pas pu être supprimés)¦$1건을 완전히 삭제했습니다 ($2건은 삭제할 수 없었습니다)
^デスクで削除した書類や、上書きする前の版は、そのフォルダの中に作る「_削除予定」フォルダに移します（必要になったときに自動で作ります）。\nこれは Windows や Mac のごみ箱ではありません。中の書類はデスクの［元に戻す］で戻せます。\n不要になったら、左の一覧で「_削除予定」フォルダを右クリックし、［空にする］で完全に削除できます。$¦Documents you delete on the desk, and the previous versions of overwritten files, are moved to a "_削除予定" folder created inside that folder (only when needed).\nThis is not the Windows or Mac trash. You can bring documents back with [Undo] on the desk.\nWhen you no longer need them, right-click the "_削除予定" folder in the list on the left and choose [Empty] to delete them permanently.¦在桌面上删除的文档以及覆盖前的旧版本，会移到该文件夹内的"_削除予定"文件夹（需要时自动创建）。\n这不是 Windows 或 Mac 的回收站。可用桌面的［撤销］恢复其中的文档。\n不再需要时，在左侧列表中右键单击"_削除予定"文件夹，选择［清空］即可永久删除。¦在桌面上刪除的文件以及覆寫前的舊版本，會移到該資料夾內的「_削除予定」資料夾（需要時自動建立）。\n這不是 Windows 或 Mac 的垃圾桶。可用桌面的［復原］還原其中的文件。\n不再需要時，在左側清單中右鍵點擊「_削除予定」資料夾，選擇［清空］即可永久刪除。¦Os documentos excluídos na mesa e as versões anteriores de arquivos sobrescritos vão para uma pasta "_削除予定" criada dentro dessa pasta (só quando necessário).\nEla não é a lixeira do Windows ou do Mac. Você pode recuperar os documentos com [Desfazer] na mesa.\nQuando não precisar mais deles, clique com o botão direito na pasta "_削除予定" na lista à esquerda e escolha [Esvaziar] para excluí-los definitivamente.¦Les documents supprimés sur le bureau et les anciennes versions des fichiers écrasés sont déplacés dans un dossier « _削除予定 » créé à l'intérieur de ce dossier (seulement si nécessaire).\nCe n'est pas la corbeille de Windows ou du Mac. Vous pouvez récupérer les documents avec [Annuler] sur le bureau.\nQuand vous n'en avez plus besoin, faites un clic droit sur le dossier « _削除予定 » dans la liste de gauche et choisissez [Vider] pour les supprimer définitivement.¦데스크에서 삭제한 문서와 덮어쓰기 전의 이전 버전은 그 폴더 안에 만드는 '_削除予定' 폴더로 옮깁니다 (필요할 때 자동으로 만듭니다).\n이것은 Windows나 Mac의 휴지통이 아닙니다. 안의 문서는 데스크의 [실행 취소]로 되돌릴 수 있습니다.\n필요 없어지면 왼쪽 목록에서 '_削除予定' 폴더를 오른쪽 클릭하고 [비우기]로 완전히 삭제할 수 있습니다.
^(\d+) 件$¦$1 item(s)¦$1 项¦$1 項¦$1 item(s)¦$1 élément(s)¦$1건
^(\d+) 件 ／ 選択 (\d+)$¦$1 item(s) / $2 selected¦$1 项 ／ 已选 $2¦$1 項 ／ 已選 $2¦$1 item(s) / $2 selecionado(s)¦$1 élément(s) / $2 sélectionné(s)¦$1건 / 선택 $2
^(\d+) 件（絞り込み中） ／ 選択 (\d+)$¦$1 item(s) (filtered) / $2 selected¦$1 项（筛选中） ／ 已选 $2¦$1 項（篩選中） ／ 已選 $2¦$1 item(s) (filtrado) / $2 selecionado(s)¦$1 élément(s) (filtré) / $2 sélectionné(s)¦$1건 (필터 중) / 선택 $2
^(\d+) 件を「_削除予定」へ移しました（Ctrl\+Z で戻せます）$¦Moved $1 item(s) to "_削除予定" (Ctrl+Z to undo)¦已将 $1 项移到"_削除予定"（可按Ctrl+Z撤销）¦已將 $1 項移到「_削除予定」（可按Ctrl+Z復原）¦$1 item(s) movido(s) para "_削除予定" (Ctrl+Z para desfazer)¦$1 élément(s) déplacé(s) vers « _削除予定 » (Ctrl+Z pour annuler)¦$1건을 '_削除予定'(으)로 옮겼습니다 (Ctrl+Z로 되돌리기)
^(\d+) 件を「(.+)」へ移動しました（Ctrl\+Z で戻せます）$¦Moved $1 item(s) to "$2" (Ctrl+Z to undo)¦已将 $1 项移到"$2"（可按Ctrl+Z撤销）¦已將 $1 項移到「$2」（可按Ctrl+Z復原）¦$1 item(s) movido(s) para "$2" (Ctrl+Z para desfazer)¦$1 élément(s) déplacé(s) vers « $2 » (Ctrl+Z pour annuler)¦$1건을 '$2'(으)로 이동했습니다 (Ctrl+Z로 되돌리기)
^(\d+) 件を貼り付けました（Ctrl\+Z で戻せます）$¦Pasted $1 item(s) (Ctrl+Z to undo)¦已粘贴 $1 项（可按Ctrl+Z撤销）¦已貼上 $1 項（可按Ctrl+Z復原）¦$1 item(s) colado(s) (Ctrl+Z para desfazer)¦$1 élément(s) collé(s) (Ctrl+Z pour annuler)¦$1건을 붙여넣었습니다 (Ctrl+Z로 되돌리기)
^(\d+) 件をコピーしました（Ctrl\+V で貼り付け）$¦Copied $1 item(s) (Ctrl+V to paste)¦已复制 $1 项（按Ctrl+V粘贴）¦已複製 $1 項（按Ctrl+V貼上）¦$1 item(s) copiado(s) (Ctrl+V para colar)¦$1 élément(s) copié(s) (Ctrl+V pour coller)¦$1건을 복사했습니다 (Ctrl+V로 붙여넣기)
^(\d+) 件を「(.+)」に取り込みました（コピー）$¦Imported $1 item(s) into "$2" (copied)¦已将 $1 项导入"$2"（复制）¦已將 $1 項匯入「$2」（複製）¦$1 item(s) importado(s) para "$2" (cópia)¦$1 élément(s) importé(s) dans « $2 » (copie)¦$1건을 '$2'에 가져왔습니다 (복사)
^PDF・作業ファイル・JPG・PNG 以外は取り込めません：(.+)$¦Only PDF, work files, JPG and PNG can be imported: $1¦只能导入PDF、工作文件、JPG、PNG：$1¦只能匯入PDF、工作檔案、JPG、PNG：$1¦Só é possível importar PDF, arquivos de trabalho, JPG e PNG: $1¦Seuls les PDF, fichiers de travail, JPG et PNG peuvent être importés : $1¦PDF・작업 파일・JPG・PNG 외에는 가져올 수 없습니다: $1
^「(.+)」を作りました（Ctrl\+Z で結合前に戻せます）$¦Created "$1" (Ctrl+Z to undo the merge)¦已创建"$1"（可按Ctrl+Z恢复到合并前）¦已建立「$1」（可按Ctrl+Z還原到合併前）¦"$1" criado (Ctrl+Z para desfazer a união)¦« $1 » créé (Ctrl+Z pour annuler la fusion)¦'$1'을(를) 만들었습니다 (Ctrl+Z로 결합 전으로 되돌리기)
^「(.+)」がすでにあります。別の名前（番号付き）で保存します。$¦"$1" already exists. It will be saved under another name (numbered).¦"$1"已存在。将以其他名称（带编号）保存。¦「$1」已存在。將以其他名稱（帶編號）儲存。¦"$1" já existe. Será salvo com outro nome (numerado).¦« $1 » existe déjà. Il sera enregistré sous un autre nom (numéroté).¦'$1'이(가) 이미 있습니다. 다른 이름(번호 붙임)으로 저장합니다.
^結合しています\.\.\. (\d+) / (\d+)$¦Merging... $1 / $2¦正在合并... $1 / $2¦正在合併... $1 / $2¦Unindo... $1 / $2¦Fusion... $1 / $2¦결합하는 중... $1 / $2
^分けています\.\.\. (.+) (\d+) / (\d+)$¦Splitting... $1 $2 / $3¦正在拆分... $1 $2 / $3¦正在拆分... $1 $2 / $3¦Separando... $1 $2 / $3¦Séparation... $1 $2 / $3¦나누는 중... $1 $2 / $3
^(\d+) 個のファイルに分けました（フォルダ「(.+)」）。Ctrl\+Z で元に戻せます$¦Split into $1 file(s) (folder "$2"). Ctrl+Z to undo¦已拆分为 $1 个文件（文件夹"$2"）。可按Ctrl+Z撤销¦已拆分為 $1 個檔案（資料夾「$2」）。可按Ctrl+Z復原¦Separado em $1 arquivo(s) (pasta "$2"). Ctrl+Z para desfazer¦Séparé en $1 fichier(s) (dossier « $2 »). Ctrl+Z pour annuler¦$1개 파일로 나눴습니다(폴더 "$2"). Ctrl+Z로 되돌리기
^(\d+) 個のファイルに分けました。Ctrl\+Z で元に戻せます$¦Split into $1 file(s). Ctrl+Z to undo¦已拆分为 $1 个文件。可按Ctrl+Z撤销¦已拆分為 $1 個檔案。可按Ctrl+Z復原¦Separado em $1 arquivo(s). Ctrl+Z para desfazer¦Séparé en $1 fichier(s). Ctrl+Z pour annuler¦$1개 파일로 나눴습니다. Ctrl+Z로 되돌리기
^(\d+) 個のファイルを、1ページずつ別のファイル（合計 (\d+) 個）に分けます。作業ファイルは書き込み・付箋を残したまま、1ページずつの作業ファイル（\.frontpdf）になります。$¦Split $1 file(s) into one file per page ($2 in total). Work files become one-page work files (.frontpdf) with markups and notes kept.¦将 $1 个文件按页拆分为单独的文件（共 $2 个）。工作文件会保留批注和便签，成为单页工作文件（.frontpdf）。¦將 $1 個檔案按頁拆分為單獨的檔案（共 $2 個）。工作檔案會保留註記和便利貼，成為單頁工作檔案（.frontpdf）。¦Separar $1 arquivo(s) em um arquivo por página ($2 no total). Arquivos de trabalho viram arquivos de trabalho de uma página (.frontpdf), mantendo anotações e notas.¦Séparer $1 fichier(s) en un fichier par page ($2 au total). Les fichiers de travail deviennent des fichiers de travail d'une page (.frontpdf), annotations et notes conservées.¦$1개 파일을 페이지별 파일(총 $2개)로 나눕니다. 작업 파일은 필기·메모를 유지한 채 1페이지 작업 파일(.frontpdf)이 됩니다.
^「(.+)」を、1ページずつ別のファイル（合計 (\d+) 個）に分けます。作業ファイルは書き込み・付箋を残したまま、1ページずつの作業ファイル（\.frontpdf）になります。$¦Split "$1" into one file per page ($2 in total). Work files become one-page work files (.frontpdf) with markups and notes kept.¦将"$1"按页拆分为单独的文件（共 $2 个）。工作文件会保留批注和便签，成为单页工作文件（.frontpdf）。¦將「$1」按頁拆分為單獨的檔案（共 $2 個）。工作檔案會保留註記和便利貼，成為單頁工作檔案（.frontpdf）。¦Separar "$1" em um arquivo por página ($2 no total). Arquivos de trabalho viram arquivos de trabalho de uma página (.frontpdf), mantendo anotações e notas.¦Séparer « $1 » en un fichier par page ($2 au total). Les fichiers de travail deviennent des fichiers de travail d'une page (.frontpdf), annotations et notes conservées.¦"$1"을(를) 페이지별 파일(총 $2개)로 나눕니다. 작업 파일은 필기·메모를 유지한 채 1페이지 작업 파일(.frontpdf)이 됩니다.
^(\d+) 個の PDF に分けました（フォルダ「(.+)」）。Ctrl\+Z で元に戻せます$¦Split into $1 PDF(s) (folder "$2"). Ctrl+Z to undo¦已拆分为 $1 个PDF（文件夹"$2"）。可按Ctrl+Z撤销¦已拆分為 $1 個PDF（資料夾「$2」）。可按Ctrl+Z復原¦Separado em $1 PDF(s) (pasta "$2"). Ctrl+Z para desfazer¦Séparé en $1 PDF (dossier « $2 »). Ctrl+Z pour annuler¦PDF $1개로 나눴습니다 (폴더 '$2'). Ctrl+Z로 되돌리기
^(\d+) 個の PDF に分けました。Ctrl\+Z で元に戻せます$¦Split into $1 PDF(s). Ctrl+Z to undo¦已拆分为 $1 个PDF。可按Ctrl+Z撤销¦已拆分為 $1 個PDF。可按Ctrl+Z復原¦Separado em $1 PDF(s). Ctrl+Z para desfazer¦Séparé en $1 PDF. Ctrl+Z pour annuler¦PDF $1개로 나눴습니다. Ctrl+Z로 되돌리기
^(\d+) 個の PDFを、1ページずつ別の PDF（合計 (\d+) 個）に分けます。名前は「元の名前_p01\.pdf」のようになります。$¦Split $1 PDF(s) into one PDF per page ($2 in total). Names will look like "original_p01.pdf".¦将 $1 个PDF按每页拆分为单独的PDF（共 $2 个）。名称类似"原名_p01.pdf"。¦將 $1 個PDF按每頁拆分為單獨的PDF（共 $2 個）。名稱類似「原名_p01.pdf」。¦Separar $1 PDF(s) em um PDF por página ($2 no total). Os nomes ficarão como "original_p01.pdf".¦Séparer $1 PDF en un PDF par page ($2 au total). Les noms seront du type « original_p01.pdf ».¦PDF $1개를 1페이지씩 별도 PDF(총 $2개)로 나눕니다. 이름은 '원래이름_p01.pdf'처럼 됩니다.
^「(.+)」を、1ページずつ別の PDF（合計 (\d+) 個）に分けます。名前は「元の名前_p01\.pdf」のようになります。$¦Split "$1" into one PDF per page ($2 in total). Names will look like "original_p01.pdf".¦将"$1"按每页拆分为单独的PDF（共 $2 个）。名称类似"原名_p01.pdf"。¦將「$1」按每頁拆分為單獨的PDF（共 $2 個）。名稱類似「原名_p01.pdf」。¦Separar "$1" em um PDF por página ($2 no total). Os nomes ficarão como "original_p01.pdf".¦Séparer « $1 » en un PDF par page ($2 au total). Les noms seront du type « original_p01.pdf ».¦'$1'을(를) 1페이지씩 별도 PDF(총 $2개)로 나눕니다. 이름은 '원래이름_p01.pdf'처럼 됩니다.
^フォルダ「(.+)」を作りました$¦Created folder "$1"¦已创建文件夹"$1"¦已建立資料夾「$1」¦Pasta "$1" criada¦Dossier « $1 » créé¦폴더 '$1'을(를) 만들었습니다
^移動先に同じ名前の「(.+)」があります$¦"$1" already exists in the destination¦目标位置已有同名的"$1"¦目的地已有同名的「$1」¦"$1" já existe no destino¦« $1 » existe déjà dans la destination¦이동할 곳에 같은 이름의 '$1'이(가) 있습니다
^フォルダを読めませんでした: (.+)$¦Could not read the folder: $1¦无法读取文件夹：$1¦無法讀取資料夾：$1¦Não foi possível ler a pasta: $1¦Impossible de lire le dossier : $1¦폴더를 읽을 수 없었습니다: $1
^戻せませんでした（ファイルが移動・変更されている可能性）：(.+)$¦Could not undo (the file may have been moved or changed): $1¦无法撤销（文件可能已被移动或更改）：$1¦無法復原（檔案可能已被移動或變更）：$1¦Não foi possível desfazer (o arquivo pode ter sido movido ou alterado): $1¦Impossible d'annuler (le fichier a peut-être été déplacé ou modifié) : $1¦되돌릴 수 없었습니다 (파일이 이동・변경되었을 수 있음): $1
^元に戻しました：(.+)$¦Undone: $1¦已撤销：$1¦已復原：$1¦Desfeito: $1¦Annulé : $1¦실행 취소했습니다: $1
^やり直しました：(.+)$¦Redone: $1¦已重做：$1¦已重做：$1¦Refeito: $1¦Rétabli : $1¦다시 실행했습니다: $1
^選んだ (\d+) 件を印刷$¦Print $1 selected¦打印所选 $1 项¦列印所選 $1 項¦Imprimir $1 selecionado(s)¦Imprimer les $1 sélectionnés¦선택한 $1건 인쇄
^選んだ (\d+) 件を結合$¦Merge $1 selected¦合并所选 $1 项¦合併所選 $1 項¦Unir $1 selecionado(s)¦Fusionner les $1 sélectionnés¦선택한 $1건 결합
^同じフォルダに「(.+)」があります。上書きしますか？$¦"$1" already exists in this folder. Overwrite it?¦同一文件夹中已有"$1"。要覆盖吗？¦同一資料夾中已有「$1」。要覆寫嗎？¦"$1" já existe nesta pasta. Sobrescrever?¦« $1 » existe déjà dans ce dossier. L'écraser ?¦같은 폴더에 '$1'이(가) 있습니다. 덮어쓸까요?
^同じフォルダに「(.+)」があります。上書きしますか？\n（上書き前の版は「_削除予定」フォルダに残します）$¦"$1" already exists in this folder. Overwrite it?\n(The previous version is kept in the "_削除予定" folder)¦同一文件夹中已有"$1"。要覆盖吗？\n（旧版本会保留在"_削除予定"文件夹）¦同一資料夾中已有「$1」。要覆寫嗎？\n（舊版本會保留在「_削除予定」資料夾）¦"$1" já existe nesta pasta. Sobrescrever?\n(A versão anterior fica na pasta "_削除予定")¦« $1 » existe déjà dans ce dossier. L'écraser ?\n(L'ancienne version est conservée dans le dossier « _削除予定 »)¦같은 폴더에 '$1'이(가) 있습니다. 덮어쓸까요?\n(이전 버전은 '_削除予定' 폴더에 남깁니다)
^元のファイル「(.+)」に上書きします。\n上書き前の版は「_削除予定」フォルダに残し、デスクの［元に戻す］で戻せます。$¦Overwrite the original file "$1".\nThe previous version is kept in the "_削除予定" folder and can be restored with [Undo] on the desk.¦将覆盖原文件"$1"。\n旧版本会保留在"_削除予定"文件夹，可用桌面的［撤销］恢复。¦將覆寫原檔案「$1」。\n舊版本會保留在「_削除予定」資料夾，可用桌面的［復原］還原。¦O arquivo original "$1" será sobrescrito.\nA versão anterior fica na pasta "_削除予定" e pode ser recuperada com [Desfazer] na mesa.¦Le fichier d'origine « $1 » va être écrasé.\nL'ancienne version est conservée dans « _削除予定 » et peut être restaurée avec [Annuler] sur le bureau.¦원본 파일 '$1'에 덮어씁니다.\n이전 버전은 '_削除予定' 폴더에 남기며, 데스크의 [실행 취소]로 되돌릴 수 있습니다.
^「(.+)」に上書きしました（前の版は _削除予定 に残しました）$¦Overwrote "$1" (the previous version is in _削除予定)¦已覆盖"$1"（旧版本保留在 _削除予定）¦已覆寫「$1」（舊版本保留在 _削除予定）¦"$1" sobrescrito (a versão anterior está em _削除予定)¦« $1 » écrasé (l'ancienne version est dans _削除予定)¦'$1'에 덮어썼습니다 (이전 버전은 _削除予定에 남김)
^「(.+)」を元のフォルダに保存しました$¦Saved "$1" in the original folder¦已将"$1"保存到原文件夹¦已將「$1」儲存到原資料夾¦"$1" salvo na pasta original¦« $1 » enregistré dans le dossier d'origine¦'$1'을(를) 원래 폴더에 저장했습니다
^上書き保存しました（前の版はデスクの「_削除予定」に残しています）$¦Saved (overwritten). The previous version is in "_削除予定" on the desk¦已覆盖保存（旧版本保留在桌面的"_削除予定"）¦已覆寫儲存（舊版本保留在桌面的「_削除予定」）¦Salvo (sobrescrito). A versão anterior está em "_削除予定" na mesa¦Enregistré (écrasé). L'ancienne version est dans « _削除予定 » sur le bureau¦덮어써서 저장했습니다 (이전 버전은 데스크의 '_削除予定'에 있음)
^上書き保存しました（前の版はデスクの「_削除予定」に残しています）（(\d+) ページは画像化）$¦Saved (overwritten). The previous version is in "_削除予定" on the desk ($1 page(s) rasterized)¦已覆盖保存（旧版本保留在桌面的"_削除予定"）（$1 页已转为图像）¦已覆寫儲存（舊版本保留在桌面的「_削除予定」）（$1 頁已轉為影像）¦Salvo (sobrescrito). A versão anterior está em "_削除予定" na mesa ($1 página(s) rasterizada(s))¦Enregistré (écrasé). L'ancienne version est dans « _削除予定 » sur le bureau ($1 page(s) rastérisée(s))¦덮어써서 저장했습니다 (이전 버전은 데스크의 '_削除予定'에 있음) ($1페이지 이미지화)
^PDF「(.+)」を保存しました$¦Saved PDF "$1"¦已保存PDF"$1"¦已儲存PDF「$1」¦PDF "$1" salvo¦PDF « $1 » enregistré¦PDF '$1'을(를) 저장했습니다
^PDF「(.+)」を保存しました（(\d+) ページは画像化）$¦Saved PDF "$1" ($2 page(s) rasterized)¦已保存PDF"$1"（$2 页已转为图像）¦已儲存PDF「$1」（$2 頁已轉為影像）¦PDF "$1" salvo ($2 página(s) rasterizada(s))¦PDF « $1 » enregistré ($2 page(s) rastérisée(s))¦PDF '$1'을(를) 저장했습니다 ($2페이지 이미지화)
^(\d+) 個のPDFを保存しました$¦Saved $1 PDF(s)¦已保存 $1 个PDF¦已儲存 $1 個PDF¦$1 PDF(s) salvo(s)¦$1 PDF enregistré(s)¦PDF $1개를 저장했습니다
^(\d+) 個のPDFを保存しました（(\d+) ページは画像化：文字データなし）$¦Saved $1 PDF(s) ($2 page(s) rasterized: no text data)¦已保存 $1 个PDF（$2 页已转为图像：无文字数据）¦已儲存 $1 個PDF（$2 頁已轉為影像：無文字資料）¦$1 PDF(s) salvo(s) ($2 página(s) rasterizada(s): sem texto)¦$1 PDF enregistré(s) ($2 page(s) rastérisée(s) : sans texte)¦PDF $1개를 저장했습니다 ($2페이지 이미지화: 텍스트 없음)
^作業ファイル「(.+)」を保存しました（人に渡すときは［PDF保存］を使ってください）$¦Saved work file "$1" (use [Save PDF] when sharing with others)¦已保存工作文件"$1"（交给他人时请使用［保存PDF］）¦已儲存工作檔案「$1」（交給他人時請使用［儲存PDF］）¦Arquivo de trabalho "$1" salvo (use [Salvar PDF] para compartilhar)¦Fichier de travail « $1 » enregistré (utilisez [Enregistrer PDF] pour partager)¦작업 파일 '$1'을(를) 저장했습니다 (다른 사람에게 줄 때는 [PDF 저장]을 사용하세요)
^(\d+) ページ ／ 選択 (\d+)$¦$1 pages / $2 selected¦$1 页 / 已选 $2¦$1 頁 / 已選 $2¦$1 páginas / $2 selecionadas¦$1 pages / $2 sélectionnées¦$1페이지 / 선택 $2
^(\d+)件$¦$1 hits¦$1 个¦$1 個¦$1 resultados¦$1 résultats¦$1건
^(\d+) 箇所を黒塗りしました（書き出し時は「画像化してPDF出力」を選んでください）　※Ctrl\+Z で戻せます$¦Blacked out $1 places (when exporting, choose "Rasterize masked pages") * Ctrl+Z to undo¦已涂黑 $1 处（导出时请选择"转为图像后导出PDF"）※可按Ctrl+Z撤销¦已塗黑 $1 處（匯出時請選擇「轉為影像後匯出PDF」）※可按Ctrl+Z復原¦$1 locais tarjados (ao exportar, escolha "converter em imagem") * Ctrl+Z para desfazer¦$1 zones noircies (à l'export, choisissez « convertir en image ») * Ctrl+Z pour annuler¦$1곳을 검게 칠했습니다 (내보낼 때 "이미지로 바꿔 PDF 출력"을 선택하세요) ※Ctrl+Z로 되돌리기
^(\d+) 箇所をマーカーしました　※Ctrl\+Z で戻せます$¦Highlighted $1 places * Ctrl+Z to undo¦已高亮 $1 处 ※可按Ctrl+Z撤销¦已醒目標示 $1 處 ※可按Ctrl+Z復原¦$1 locais destacados * Ctrl+Z para desfazer¦$1 zones surlignées * Ctrl+Z pour annuler¦$1곳을 강조했습니다 ※Ctrl+Z로 되돌리기
^(\d+) 個のファイルを追加しました$¦Added $1 file(s)¦已添加 $1 个文件¦已新增 $1 個檔案¦$1 arquivo(s) adicionado(s)¦$1 fichier(s) ajouté(s)¦파일 $1개를 추가했습니다
^(\d+) 文字をコピーしました（表形式：Excelにそのまま貼り付けできます）$¦Copied $1 characters (table format: paste straight into Excel)¦已复制 $1 个字（表格格式：可直接粘贴到Excel）¦已複製 $1 個字（表格格式：可直接貼到Excel）¦$1 caracteres copiados (formato tabela: cole direto no Excel)¦$1 caractères copiés (format tableau : collez directement dans Excel)¦$1자를 복사했습니다 (표 형식: Excel에 그대로 붙여넣기 가능)
^(\d+) 文字をコピーしました$¦Copied $1 characters¦已复制 $1 个字¦已複製 $1 個字¦$1 caracteres copiados¦$1 caractères copiés¦$1자를 복사했습니다
^(\d+) 文字を選択しました ― Ctrl\+C でコピー$¦Selected $1 characters — Ctrl+C to copy¦已选择 $1 个字 — 按Ctrl+C复制¦已選取 $1 個字 — 按Ctrl+C複製¦$1 caracteres selecionados — Ctrl+C para copiar¦$1 caractères sélectionnés — Ctrl+C pour copier¦$1자를 선택했습니다 — Ctrl+C로 복사
^(\d+) 文字を選択中$¦$1 characters selected¦已选 $1 个字¦已選 $1 個字¦$1 caracteres selecionados¦$1 caractères sélectionnés¦$1자 선택 중
^Front PDF ― (.+)$¦Front PDF — $1¦Front PDF — $1¦Front PDF — $1¦Front PDF — $1¦Front PDF — $1¦Front PDF — $1
^(.+) の (\d+) ページ目$¦$1 – page $2¦$1 第 $2 页¦$1 第 $2 頁¦$1 – página $2¦$1 – page $2¦$1의 $2페이지
^「(.+)」が (\d+) 件見つかりました（Enterで次へ）$¦Found $2 matches for "$1" (Enter for next)¦找到"$1" $2 处（按Enter到下一个）¦找到「$1」$2 處（按Enter到下一個）¦$2 resultados para "$1" (Enter para o próximo)¦$2 résultat(s) pour « $1 » (Entrée pour suivant)¦"$1"을(를) $2건 찾았습니다 (Enter로 다음)
^「(.+)」は見つかりませんでした（スキャン画像のPDFは検索できません）$¦"$1" was not found (scanned PDFs can't be searched)¦未找到"$1"（扫描的PDF无法搜索）¦找不到「$1」（掃描的PDF無法搜尋）¦"$1" não encontrado (PDFs digitalizados não podem ser pesquisados)¦« $1 » introuvable (les PDF numérisés ne sont pas cherchables)¦"$1"을(를) 찾지 못했습니다 (스캔 PDF는 검색 불가)
^「(.+)」ツール$¦"$1" tool¦"$1"工具¦「$1」工具¦ferramenta "$1"¦outil « $1 »¦'$1' 도구
^選んでいた(.+)$¦the selected $1¦所选的$1¦所選的$1¦$1 selecionado(a)¦$1 sélectionné(e)¦선택했던 $1
^(.+) のプロパティ$¦$1 properties¦$1 属性¦$1 屬性¦Propriedades: $1¦Propriétés : $1¦$1 속성
^(.+) の設定$¦$1 settings¦$1 设置¦$1 設定¦Configurações: $1¦Réglages : $1¦$1 설정
^ページ全体 \((\d+)%\)$¦Fit page ($1%)¦整页 ($1%)¦整頁 ($1%)¦Página inteira ($1%)¦Page entière ($1%)¦페이지 전체 ($1%)
^ページ幅 \((\d+)%\)$¦Fit width ($1%)¦页宽 ($1%)¦頁寬 ($1%)¦Largura da página ($1%)¦Largeur de page ($1%)¦페이지 너비 ($1%)
^範囲の書き方が正しくありません: (.+)$¦Invalid range: $1¦范围格式不正确：$1¦範圍格式不正確：$1¦Intervalo inválido: $1¦Plage non valide : $1¦범위 형식이 올바르지 않습니다: $1
^範囲外です: (.+)（全(\d+)ページ）$¦Out of range: $1 ($2 pages total)¦超出范围：$1（共 $2 页）¦超出範圍：$1（共 $2 頁）¦Fora do intervalo: $1 ($2 páginas no total)¦Hors limites : $1 ($2 pages au total)¦범위 밖입니다: $1 (전체 $2페이지)
^色 (#[0-9a-f]{6}) を拾いました。下の色をクリックしてからツールを選ぶか、ツールを選んだ状態でスポイトを使うとその色になります$¦Picked $1. Choose a tool next (or use the eyedropper with a tool active) to apply it¦已拾取 $1。接着选择工具（或在选中工具时使用吸管）即可套用¦已擷取 $1。接著選擇工具（或在選取工具時使用滴管）即可套用¦Cor $1 capturada. Escolha uma ferramenta (ou use o conta-gotas com uma ferramenta ativa) para aplicar¦Couleur $1 prélevée. Choisissez un outil (ou utilisez la pipette avec un outil actif) pour l'appliquer¦$1 색을 가져왔습니다. 도구를 고르거나, 도구를 고른 상태에서 스포이트를 쓰면 그 색이 됩니다
^色を拾いました (#[0-9a-f]{6})（(.+)の色にしました）$¦Picked $1 (set as the $2 color)¦已拾取 $1（设为$2的颜色）¦已擷取 $1（設為$2的顏色）¦Cor $1 capturada (definida para $2)¦Couleur $1 prélevée (appliquée à $2)¦$1 색을 가져왔습니다 ($2의 색으로 설정)
^色 (#[0-9a-f]{6}) を選んでいた(.+)にセットしました$¦Set $1 on the selected $2¦已将 $1 设置到所选的$2¦已將 $1 設定到所選的$2¦Cor $1 aplicada ao(à) $2 selecionado(a)¦Couleur $1 appliquée à $2 sélectionné(e)¦$1 색을 선택했던 $2에 설정했습니다
^色 (#[0-9a-f]{6}) を「(.+)」にセットしました$¦Set $1 on the "$2" tool¦已将 $1 设置到"$2"¦已將 $1 設定到「$2」¦Cor $1 aplicada à ferramenta "$2"¦Couleur $1 appliquée à l'outil « $2 »¦$1 색을 '$2'에 설정했습니다
^(.+) を読み込み中\.\.\.$¦Loading $1...¦正在读取 $1...¦正在讀取 $1...¦Carregando $1...¦Chargement de $1...¦$1 불러오는 중...
^(\d+) ページを削除しました（Ctrl\+Z で戻せます）$¦Deleted $1 page(s) (Ctrl+Z to undo)¦已删除 $1 页（可按Ctrl+Z撤销）¦已刪除 $1 頁（可按Ctrl+Z復原）¦$1 página(s) excluída(s) (Ctrl+Z para desfazer)¦$1 page(s) supprimée(s) (Ctrl+Z pour annuler)¦$1페이지를 삭제했습니다 (Ctrl+Z로 되돌리기)
^(\d+) ページを移動しました$¦Moved $1 page(s)¦已移动 $1 页¦已移動 $1 頁¦$1 página(s) movida(s)¦$1 page(s) déplacée(s)¦$1페이지를 이동했습니다
^(\d+) 個のPDFを書き出しました$¦Exported $1 PDF(s)¦已导出 $1 个PDF¦已匯出 $1 個PDF¦$1 PDF(s) exportado(s)¦$1 PDF exporté(s)¦PDF $1개를 내보냈습니다
^(\d+) 個のPDFを書き出しました（(\d+) ページは画像化：文字データなし）$¦Exported $1 PDF(s) ($2 page(s) rasterized: no text data)¦已导出 $1 个PDF（$2 页已转为图像：无文字数据）¦已匯出 $1 個PDF（$2 頁已轉為影像：無文字資料）¦$1 PDF(s) exportado(s) ($2 página(s) em imagem: sem texto)¦$1 PDF exporté(s) ($2 page(s) en image : sans texte)¦PDF $1개를 내보냈습니다 ($2페이지는 이미지화: 텍스트 데이터 없음)
^(\d+) 枚のPNGを書き出しました$¦Exported $1 PNG(s)¦已导出 $1 张PNG¦已匯出 $1 張PNG¦$1 PNG(s) exportado(s)¦$1 PNG exporté(s)¦PNG $1장을 내보냈습니다
^画像 (\d+) / (\d+) を作成中\.\.\.$¦Creating image $1 / $2...¦正在生成图片 $1 / $2...¦正在產生圖片 $1 / $2...¦Criando imagem $1 / $2...¦Création de l'image $1 / $2...¦이미지 $1 / $2 만드는 중...
^ファイル (\d+) / (\d+)　ページ (\d+) / (\d+) を処理中\.\.\.$¦File $1 / $2 — processing page $3 / $4...¦文件 $1 / $2　正在处理第 $3 / $4 页...¦檔案 $1 / $2　正在處理第 $3 / $4 頁...¦Arquivo $1 / $2 — processando página $3 / $4...¦Fichier $1 / $2 — traitement de la page $3 / $4...¦파일 $1 / $2　페이지 $3 / $4 처리 중...
^ページ (\d+) / (\d+) を処理中\.\.\.$¦Processing page $1 / $2...¦正在处理第 $1 / $2 页...¦正在處理第 $1 / $2 頁...¦Processando página $1 / $2...¦Traitement de la page $1 / $2...¦페이지 $1 / $2 처리 중...
^検索中\.\.\. (\d+) / (\d+) ページ$¦Searching... page $1 / $2¦搜索中... 第 $1 / $2 页¦搜尋中... 第 $1 / $2 頁¦Buscando... página $1 / $2¦Recherche... page $1 / $2¦검색 중... $1 / $2페이지
^他の (\d+) ページの同じ位置に入れました$¦Placed at the same spot on $1 other page(s)¦已放到其他 $1 页的相同位置¦已放到其他 $1 頁的相同位置¦Colocado na mesma posição em $1 outra(s) página(s)¦Placé au même endroit sur $1 autre(s) page(s)¦다른 $1페이지의 같은 위치에 넣었습니다
^この設定を「(.+)」の既定にしました$¦Saved as the default for "$1"¦已设为"$1"的默认¦已設為「$1」的預設¦Definido como padrão de "$1"¦Défini par défaut pour « $1 »¦이 설정을 '$1'의 기본값으로 했습니다
^(.+)の色を変えました$¦Changed the $1 color¦已更改$1的颜色¦已變更$1的顏色¦Cor de $1 alterada¦Couleur de $1 modifiée¦$1의 색을 바꿨습니다
^作業ファイル「(.+)」を保存しました（人に渡すときは［PDF書き出し］を使ってください）$¦Saved work file "$1" (use [Export PDF] when sharing with others)¦已保存工作文件"$1"（交给他人时请使用［导出PDF］）¦已儲存工作檔案「$1」（交給他人時請使用［匯出PDF］）¦Arquivo de trabalho "$1" salvo (para compartilhar, use [Exportar PDF])¦Fichier de travail « $1 » enregistré (pour partager, utilisez [Exporter PDF])¦작업 파일 '$1'을(를) 저장했습니다 (다른 사람에게 줄 때는 [PDF 내보내기]를 사용하세요)
^作業ファイル「(.+)」を開きました（(\d+) ページ）$¦Opened work file "$1" ($2 pages)¦已打开工作文件"$1"（$2 页）¦已開啟工作檔案「$1」（$2 頁）¦Arquivo de trabalho "$1" aberto ($2 páginas)¦Fichier de travail « $1 » ouvert ($2 pages)¦작업 파일 '$1'을(를) 열었습니다 ($2페이지)
^作業ファイルを開いています\.\.\. (\d+)/(\d+)$¦Opening work file... $1/$2¦正在打开工作文件... $1/$2¦正在開啟工作檔案... $1/$2¦Abrindo arquivo de trabalho... $1/$2¦Ouverture du fichier de travail... $1/$2¦작업 파일 여는 중... $1/$2
^いま開いている作業を閉じて、作業ファイル「(.+)」を開きます。よろしいですか？\n（保存していない変更は失われます）$¦Close the current work and open work file "$1"?\n(Unsaved changes will be lost)¦要关闭当前工作并打开工作文件"$1"吗？\n（未保存的更改将丢失）¦要關閉目前工作並開啟工作檔案「$1」嗎？\n（未儲存的變更將遺失）¦Fechar o trabalho atual e abrir o arquivo "$1"?\n(Alterações não salvas serão perdidas)¦Fermer le travail en cours et ouvrir « $1 » ?\n(Les modifications non enregistrées seront perdues)¦지금 작업을 닫고 작업 파일 '$1'을(를) 열까요?\n(저장하지 않은 변경은 사라집니다)
^(\d+) 個のハンコを読み込みました$¦Imported $1 stamp(s)¦已导入 $1 个印章¦已匯入 $1 個印章¦$1 carimbo(s) importado(s)¦$1 tampon(s) importé(s)¦도장 $1개를 불러왔습니다
^([^：\n]+)：(.+)$¦$1: $2¦$1：$2¦$1：$2¦$1: $2¦$1 : $2¦$1: $2
"""
def rows(block):
    for ln in block.strip('\n').split('\n'):
        if not ln.strip(): continue
        p=ln.split('¦'); assert len(p)==7,(len(p),ln[:60]); yield p
ex={}
for p in rows(EX):
    ex[p[0]]={L[i]:p[i+1] for i in range(6)}
pat=[[p[0].replace('\\n','\n'),{L[i]:p[i+1].replace('\\n','\n') for i in range(6)}] for p in rows(PAT)]
html={}
try:
    from i18n_html import HTML
    for k,v in HTML.items(): html[' '.join(k.split())]=v
except ImportError: pass
json.dump({'ex':ex,'pat':pat,'html':html},open('i18n.json','w',encoding='utf-8'),ensure_ascii=False)
print('ex',len(ex),'pat',len(pat),'html',len(html))
