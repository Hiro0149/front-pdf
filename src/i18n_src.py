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
表示されたパスワードを下に貼り付け¦Paste the password shown there below¦将显示的密码粘贴到下方¦將顯示的密碼貼到下方¦Cole abaixo a senha exibida¦Collez ci-dessous le mot de passe affiché¦표시된 비밀번호를 아래에 붙여넣기
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
"""
# dynamic patterns: regex ¦ en ¦ zhCN ¦ zhTW ¦ pt ¦ fr ¦ ko   ($1.. = groups; Japanese groups get translated if known)
PAT=r"""
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
