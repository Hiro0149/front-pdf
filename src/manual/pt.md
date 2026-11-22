# Manual do Front PDF (Português) v1.0.2 (2026-11-22)

## 1. Visão geral
- O Front PDF é um editor de PDF que funciona apenas abrindo um arquivo HTML (cerca de 3,7 MB) no navegador (Edge ou Chrome recomendados). Não precisa instalar.
- Totalmente offline. Os arquivos nunca são enviados; tudo é processado no navegador do seu PC.
- Recursos: mesclar, dividir, reordenar, girar e excluir páginas de PDFs e imagens; anotar (caneta, formas, texto, notas adesivas, carimbos, emoji, imagens); tarja preta / branca; busca de texto; cópia de texto por retângulo (tabelas colam direto no Excel); marca d'água; ajuste para A4; 2 ou 4 páginas por folha; exportação PNG; arquivos de trabalho.
- Também é possível adicionar páginas em branco e montar documentos livremente, como num editor de texto.

## 2. Tela
- Barra de título (direita): Importar imagem (layout ao abrir PNG/JPEG: Colocar em A4 / Manter tamanho), Tema, Idioma (globo), ? (ajuda), ⓘ (versão e licença).
- Barra 1: Arquivo (Abrir / Salvar trabalho), Exibir (▦ Grade / ✎ Editar), Página (Pág. em branco, girar à esquerda/direita, Duplicar, Excluir página), Desfazer / Refazer e, à direita, Exportar (Exportar PNG / Exportar PDF).
- Barra 2 (só no modo de edição): ◀ número da página ▶, Zoom (− / menu / +), Buscar (caixa, ▲▼, total, Destacar tudo, Tarjar tudo), Todas (Marca d'água, Limpar anotações).
- Esquerda: miniaturas (controle Tamanho e Colunas no topo). Arraste a divisa para mudar a largura.
- Caixa de ferramentas (5 grupos), visualizador no centro, painel de propriedades à direita, barra de status embaixo.

## 3. Modos
- Modo de edição (✎ Editar): miniaturas à esquerda, anotação direto na página à direita.
- Modo grade (▦ Grade): só miniaturas grandes, para organizar páginas. Clique duplo ou Enter para editar a página.
- Duas páginas: clique numa miniatura e depois Ctrl+clique em outra. As duas aparecem lado a lado e ambas podem ser anotadas (a página ativa tem moldura). Clique numa só página para voltar.

## 4. Abrir e mesclar
- [Abrir] (Ctrl+O) ou arraste PDF / PNG / JPEG / arquivos de trabalho (.frontpdf). Quantos quiser. A ordem das miniaturas é a ordem da mesclagem.
- Imagens viram PDFs de uma página (conforme "Importar imagem").
- PDFs protegidos por senha não podem ser abertos.

## 5. Operações de página
- Selecionar: clique, Ctrl+clique (adicionar), Shift+clique (intervalo), Ctrl+A nas miniaturas (todas).
- Reordenar: arraste as miniaturas.
- Girar (↺↻), Duplicar e Excluir página (Delete) agem nas páginas selecionadas. Pág. em branco insere uma página A4 após a atual.
- Desfazer Ctrl+Z / Refazer Ctrl+Y (histórico único para páginas e anotações).

## 6. Ferramentas
- Selecionar: [Selecionar] clique para selecionar uma anotação, arraste para mover, cantos para redimensionar, setas para ajuste fino (Shift = ×10), Delete para excluir. Arrastar de um ponto vazio seleciona texto. [Sel. texto] seleciona só o texto dentro da caixa arrastada.
- Desenhar: [Caneta], [Pincel] (devagar = grosso, rápido = fino; mesa digitalizadora usa pressão; pode virar aerógrafo), [Marca-texto], [Borracha] (apaga traços onde passa e outros itens inteiros; nunca mexe no PDF original). Canetas: Shift = linha reta em passos de 45°, Ctrl = linha reta em qualquer ângulo.
- Formas: [Caixa], [Elipse], [Linha], [Seta], [Estrela], [Tabela] (linhas e colunas no painel à direita; só bordas). Shift = quadrado / círculo / linha de 45°.
- Preencher/Ocultar: [Destaque] (faixa amarela translúcida), [Branco], [Tarja], [Balde] (clique numa anotação = mudar cor; clique dentro de uma linha fechada = preencher), [Conta-gotas] (pega uma cor da página e aplica à ferramenta anterior ou à anotação selecionada; Alt+clique ao desenhar).
- Inserir: [Texto] (clique para colocar; conteúdo, tamanho, fonte, cor e fundo no painel), [Emoji] (escolha no painel e clique; Win+. também funciona), [Nota adesiva] (estilo papel; clique e digite, clique duplo para editar), [Carimbo] (escolha no caderno à direita e clique), [Imagem] (escolha um arquivo).
- Botões do painel: Excluir / Duplicar / Trazer p/ frente / Enviar p/ trás / Em todas as páginas (mesma posição nas demais) / Definir como padrão / Adicionar ao caderno.

## 7. Caderno de carimbos
- Tipos: marca de verificação (✓), hanamaru (flor de elogio), retangular, borda dupla, oval, selo redondo (1–3 caracteres na vertical), carimbo de data (linha superior, data, linha inferior), selo quadrado (4 caracteres em 2 colunas, da direita), imagem (carimbo digitalizado).
- Edite texto, cor, tamanho e formato da data (2026.11.20 / ’26.11.20 / R8.11.20 …). "Usar a data do dia" insere sempre a data de hoje.
- [A partir de imagem] registra um carimbo digitalizado (o branco fica transparente).
- Salvo automaticamente no navegador (por PC e navegador). [Exportar (backup)] gera StampBook_Front_PDF.json; [Importar] lê o arquivo.

## 8. Notas adesivas
- Notas de papel como no DocuWorks. Cores (amarelo, rosa, azul-claro, verde, laranja, roxo, branco), tamanho e cor do texto, negrito, nome do autor (memorizado).
- Ao exportar o PDF viram anotações: aparecem iguais no Acrobat e no Edge, o destinatário pode movê-las ou excluí-las e elas aparecem na lista de comentários. Ative "Gravar na página" para torná-las parte do conteúdo.
- Notas não são incluídas na exportação com 2 ou 4 páginas por folha.

## 9. Seleção, cópia e busca de texto
- [Sel. texto]: seleciona só os caracteres cujo centro está dentro da caixa. Dá para pegar só algumas colunas de uma tabela.
- Formato da cópia: Tabela (separada por tab; vira células no Excel) / Texto (separado por espaço). Ctrl+C copia, Ctrl+A seleciona a página toda.
- Busca: Ctrl+F → digite → Enter (próximo) / Shift+Enter (anterior). Ignora largura completa/meia e maiúsculas. [Destacar tudo] / [Tarjar tudo] processam todos os resultados.
- PDFs digitalizados não têm texto e não podem ser selecionados nem pesquisados (sem OCR).

## 10. Marca d'água
- [Marca d'água] adiciona a marca em todas as páginas e a seleciona. Mude texto, tamanho, ângulo, cor e intensidade no painel, ou [Remover marca d'água]. Clicar no texto da marca também a seleciona.

## 11. Colar e soltar imagens
- Ctrl+V de uma imagem copiada com a Ferramenta de Captura etc.: vai para a posição do mouse se ele estiver sobre a página; senão, para o centro da área visível, no tamanho visto na tela. Com o mouse sobre as miniaturas, vira uma nova página.
- Soltar um arquivo de imagem na página = colocar ali; nas miniaturas = nova página.
- Ctrl+V de texto cola como objeto de texto.

## 12. Exportar
- [Exportar PDF]: todas as páginas mescladas / só as selecionadas / um arquivo por página / a cada N páginas / por intervalos (ex.: 1-3, 4-6, 7). Opções: ajustar para A4, cortar margens (mm), 2 ou 4 por folha, título do documento.
- Se houver tarja preta ou branca, aparece uma confirmação. As tarjas só cobrem o texto e os dados continuam embaixo; para informações confidenciais escolha "Converter páginas tarjadas em imagem e exportar PDF (recomendado)" — só essas páginas viram imagem e o texto delas é removido.
- [Exportar PNG]: páginas selecionadas ou todas, a 96 / 150 / 300 dpi.
- As anotações são gravadas no PDF como imagem (qualquer idioma é preservado). Notas adesivas são anotações.

## 13. Arquivos de trabalho (.frontpdf)
- [Salvar trabalho] (Ctrl+S) salva um .frontpdf. Abra com [Abrir] ou arrastando para continuar com páginas, anotações, carimbos, notas e marca d'água editáveis. Dá para passar a um colega que segue as instruções das notas.
- Atenção: o arquivo de trabalho contém o PDF original, inclusive o texto sob as tarjas. Não o entregue a pessoas de fora da organização; compartilhe o PDF exportado.
- O caderno de carimbos e o histórico de desfazer não são incluídos. Alterações não salvas mostram "*" no título e geram aviso ao fechar.

## 14. Exibição e configurações
- Zoom: Página inteira / Largura da página / 25–400%, Ctrl+roda, Ctrl++ / Ctrl+−, Ctrl+0 para página inteira.
- Miniaturas: controle Tamanho, Colunas (Auto / 1–6), Ctrl+roda.
- Temas: Moderno / Escuro / PC retrô / Aqua / Portátil. Idiomas: 日本語, English, 简体中文, 繁體中文, Português, Français, 한국어. Ambos são memorizados.

## 15. Atalhos de teclado
- Ctrl+O abrir / Ctrl+S salvar trabalho / Ctrl+Z desfazer / Ctrl+Y ou Ctrl+Shift+Z refazer / Ctrl+F buscar / F3 ou Enter próximo / Shift+Enter anterior
- Delete exclui a anotação selecionada (páginas quando o foco está nas miniaturas) / setas ajuste fino (Shift = maior) / Esc desmarcar → Selecionar
- PageUp / PageDown trocar página / Ctrl+A todas as miniaturas (todo o texto em Sel. texto) / Ctrl+C copiar texto selecionado / Ctrl+V colar imagem ou texto
- Ctrl+roda, Ctrl++ / −, Ctrl+0 zoom / Ctrl+Enter concluir a digitação numa nota

## 16. Distribuição e solução de problemas
- O e-mail corporativo pode bloquear anexos .html → envie em ZIP ou use uma pasta compartilhada / Teams.
- Abrir direto da visualização do e-mail ou da nuvem impõe restrições (caderno não é memorizado, sem diálogo de salvar, sem área de transferência) → salve no PC primeiro e abra com clique duplo.
- Caderno, tema, idioma, autor das notas etc. ficam no navegador de cada PC (localStorage, prefixo pdfkobo98.). Limpar os dados do navegador apaga tudo, então faça backup do caderno.
- Não suportado: editar o texto existente do PDF, tarja real (remoção da estrutura do PDF; use a conversão da página em imagem), OCR, assinatura digital, criação de formulários.

## 17. Licença, direitos autorais e fonte oficial
- Copyright © 2026 Front Softworks. Licença: MIT License (texto completo no app em [ⓘ] → Licença MIT, e no arquivo LICENSE).
- Pela MIT License, qualquer pessoa ou empresa pode usar, copiar, modificar, redistribuir e usar comercialmente de graça. A única condição é manter o aviso de copyright e o texto da licença.
- Sem garantia: o software é fornecido "no estado em que se encontra" e o autor não assume garantia nem responsabilidade. Sempre confira o resultado exportado de documentos importantes.
- Software incluído: PDF.js (Apache License 2.0); pdf-lib, pako, @pdf-lib/standard-fonts, @pdf-lib/upng, qrcode-generator (MIT); tslib (0BSD); Adobe CMaps (BSD-3-Clause); PDFium JBIG2 (BSD-3-Clause); OpenJPEG (BSD-2-Clause). Textos das licenças: [ⓘ] → Licenças de terceiros, e THIRD_PARTY_NOTICES.txt.
- Fonte oficial: a página de releases no GitHub (a URL aparece em [ⓘ]). Arquivos obtidos em outros lugares podem ter sido modificados; o autor não se responsabiliza por problemas causados por versões modificadas.
- O autor nunca distribui o software por e-mail. Ao recomendá-lo, compartilhe a URL da fonte oficial em vez do arquivo ([ⓘ] → "Copiar texto e URL"). A tela de boas-vindas no primeiro uso também mostra a fonte oficial.
- Os PDFs exportados trazem "Front PDF v1.0.2 (Front Softworks)" e a URL oficial nas propriedades (Producer/Creator).
- No primeiro uso é preciso uma ativação gratuita (uma vez por navegador): (1) copie o "ID deste navegador" mostrado na tela (8 caracteres aleatórios gerados pelo app; sem informações do PC ou pessoais), cole em "Ativação" na página oficial e clique em "Emitir"; (2) cole no app a senha exibida (ou a senha curta de 10 caracteres). Ler o QR code da tela com o celular abre a página oficial com o ID preenchido. A senha só funciona nesse navegador, não em outros PCs ou navegadores. A página oficial não envia o ID; o cálculo é feito no navegador. Limpar os dados do navegador muda o ID; nesse caso, ative de novo. O ID pode ser copiado a qualquer momento enquanto esta tela estiver aberta (ela não pode ser fechada).
- Outros softwares da Front Softworks: ExVAN Planner (otimizador de carregamento de contêineres, https://exvan-planner.github.io/).
- Como verificar se o arquivo não foi alterado (Windows, sem instalar nada): execute `certutil -hashfile Front_PDF.html SHA256` no Prompt de Comando e confira se o valor é igual ao SHA-256 publicado na fonte oficial.
