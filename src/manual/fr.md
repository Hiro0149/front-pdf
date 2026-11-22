# Manuel de Front PDF (Français) v1.0.1 (2026-11-22)

## 1. Présentation
- Front PDF est un éditeur PDF qui fonctionne simplement en ouvrant un fichier HTML (environ 3,7 Mo) dans un navigateur (Edge ou Chrome recommandés). Aucune installation.
- Entièrement hors ligne. Les fichiers ne sont jamais envoyés : tout est traité dans le navigateur de votre PC.
- Fonctions : fusion, division, réorganisation, rotation et suppression de pages de PDF et d'images ; annotations (stylo, formes, texte, notes, tampons, émojis, images) ; masquage noir / blanc ; recherche ; copie de texte par cadre (les tableaux se collent directement dans Excel) ; filigrane ; format A4 ; 2 ou 4 pages par feuille ; export PNG ; fichiers de travail.
- Vous pouvez aussi ajouter des pages vierges et mettre en page librement, comme dans un traitement de texte.

## 2. Écran
- Barre de titre (droite) : Import d'image (mise en page à l'ouverture des PNG/JPEG : Placer sur A4 / Garder la taille), Thème, Langue (globe), ? (aide), ⓘ (version et licence).
- Barre 1 : Fichier (Ouvrir / Enregistrer), Affichage (▦ Grille / ✎ Éditer), Page (Page vierge, rotation gauche/droite, Dupliquer, Suppr. page), Annuler / Rétablir et, tout à droite, Exporter (Exporter PNG / Exporter PDF).
- Barre 2 (mode édition uniquement) : ◀ numéro de page ▶, Zoom (− / menu / +), Rechercher (zone, ▲▼, nombre, Tout surligner, Tout noircir), Toutes (Filigrane, Effacer annotations).
- Gauche : miniatures (curseur Taille et Colonnes en haut). Glissez le séparateur pour changer la largeur.
- Boîte à outils (5 groupes), visionneuse au centre, panneau de propriétés à droite, barre d'état en bas.

## 3. Modes
- Mode édition (✎ Éditer) : miniatures à gauche, annotation directe de la page à droite.
- Mode grille (▦ Grille) : seulement de grandes miniatures pour organiser les pages. Double-clic ou Entrée pour éditer une page.
- Deux pages : cliquez une miniature puis Ctrl+clic sur une autre. Les deux pages s'affichent côte à côte et sont toutes deux annotables (la page active est encadrée). Cliquez une seule page pour revenir.

## 4. Ouvrir et fusionner
- [Ouvrir] (Ctrl+O) ou glisser-déposer des PDF / PNG / JPEG / fichiers de travail (.pdfkobo). Sans limite de nombre. L'ordre des miniatures est l'ordre de fusion.
- Les images deviennent des PDF d'une page (selon « Import d'image »).
- Les PDF protégés par mot de passe ne peuvent pas être ouverts.

## 5. Opérations sur les pages
- Sélection : clic, Ctrl+clic (ajouter), Maj+clic (plage), Ctrl+A dans les miniatures (tout).
- Réorganiser : glissez les miniatures.
- Rotation (↺↻), Dupliquer et Suppr. page (Suppr) agissent sur les pages sélectionnées. Page vierge insère une page A4 après la page courante.
- Annuler Ctrl+Z / Rétablir Ctrl+Y (historique commun aux pages et annotations).

## 6. Outils
- Sélection : [Sélection] clic pour sélectionner une annotation, glisser pour déplacer, coins pour redimensionner, flèches pour ajuster (Maj = ×10), Suppr pour effacer. Glisser depuis une zone vide sélectionne du texte. [Sél. texte] ne sélectionne que le texte à l'intérieur du cadre.
- Dessiner : [Stylo], [Pinceau] (lent = épais, rapide = fin ; tablette : pression ; peut passer en aérographe), [Stylo fluo], [Gomme] (efface les traits là où vous passez, les autres éléments entiers ; ne touche jamais au PDF d'origine). Stylos : Maj = ligne droite par 45°, Ctrl = ligne droite à tout angle.
- Formes : [Cadre], [Ellipse], [Ligne], [Flèche], [Étoile], [Tableau] (lignes et colonnes dans le panneau de droite ; bordures seulement). Maj = carré / cercle / ligne à 45°.
- Remplir/Masquer : [Surligner] (bande jaune translucide), [Blanc], [Noircir], [Remplir] (clic sur une annotation = recolorer ; clic à l'intérieur d'un tracé fermé = remplir), [Pipette] (prélève une couleur sur la page et l'applique à l'outil précédent ou à l'annotation sélectionnée ; Alt+clic pendant le dessin).
- Insérer : [Texte] (cliquez pour placer ; contenu, taille, police, couleur et fond dans le panneau), [Émoji] (choisissez dans le panneau puis cliquez ; Win+. fonctionne aussi), [Note] (façon papier ; cliquez et tapez, double-clic pour modifier), [Tampon] (choisissez dans le carnet à droite puis cliquez), [Image] (choisissez un fichier).
- Boutons du panneau : Supprimer / Dupliquer / Premier plan / Arrière-plan / Sur toutes les pages (même endroit sur les autres pages) / Définir par défaut / Ajouter au carnet.

## 7. Carnet de tampons
- Types : coche (✓), hanamaru (fleur de félicitation), rectangulaire, double cadre, ovale, sceau rond (1 à 3 caractères à la verticale), dateur (ligne du haut, date, ligne du bas), sceau carré (4 caractères en 2 colonnes, de droite), image (tampon numérisé).
- Modifiez texte, couleur, taille et format de date (2026.11.20 / ’26.11.20 / R8.11.20 …). « Utiliser la date du jour » insère toujours la date du jour.
- [Depuis une image] ajoute un tampon numérisé (le blanc devient transparent).
- Enregistré automatiquement dans le navigateur (par PC et par navigateur). [Exporter (sauvegarde)] crée StampBook_Front_PDF.json ; [Importer] le relit.

## 8. Notes
- Notes façon papier comme dans DocuWorks. Couleurs (jaune, rose, bleu clair, vert, orange, violet, blanc), taille et couleur du texte, gras, nom de l'auteur (mémorisé).
- À l'export PDF, elles deviennent des annotations : Acrobat et Edge les affichent telles quelles, le destinataire peut les déplacer ou les supprimer et elles apparaissent dans la liste des commentaires. Activez « Incruster dans la page » pour les intégrer au contenu.
- Les notes ne sont pas incluses dans les exports 2 ou 4 pages par feuille.

## 9. Sélection, copie et recherche de texte
- [Sél. texte] : seuls les caractères dont le centre est dans le cadre sont sélectionnés. Vous pouvez ne prendre que certaines colonnes d'un tableau.
- Format de copie : Tableau (tabulations ; se répartit en cellules dans Excel) / Texte (séparé par des espaces). Ctrl+C copie, Ctrl+A sélectionne toute la page.
- Recherche : Ctrl+F → saisie → Entrée (suivant) / Maj+Entrée (précédent). Ignore pleine/demi-chasse et la casse. [Tout surligner] / [Tout noircir] traitent tous les résultats.
- Les PDF numérisés n'ont pas de texte et ne sont ni sélectionnables ni cherchables (pas d'OCR).

## 10. Filigrane
- [Filigrane] ajoute un filigrane à toutes les pages et le sélectionne. Modifiez texte, taille, angle, couleur et intensité dans le panneau, ou [Supprimer le filigrane]. Cliquer sur le texte du filigrane le sélectionne aussi.

## 11. Coller et déposer des images
- Ctrl+V d'une image copiée avec l'Outil Capture, etc. : placée à la position de la souris si elle est sur la page, sinon au centre de la zone visible, à la taille vue à l'écran. Si la souris est sur les miniatures, l'image est ajoutée comme nouvelle page.
- Déposer un fichier image sur la page = l'y placer ; sur les miniatures = nouvelle page.
- Ctrl+V d'un texte le colle comme objet texte.

## 12. Export
- [Exporter PDF] : toutes les pages fusionnées / pages sélectionnées / un fichier par page / toutes les N pages / par plages (ex. 1-3, 4-6, 7). Options : format A4, rognage des marges (mm), 2 ou 4 par feuille, titre du document.
- En cas de masquage noir ou blanc, une confirmation s'affiche. Les masques ne font que couvrir et le texte reste en dessous ; pour des informations confidentielles, choisissez « Convertir les pages masquées en image et exporter (recommandé) » — seules ces pages deviennent des images et leur texte est supprimé.
- [Exporter PNG] : pages sélectionnées ou toutes, à 96 / 150 / 300 dpi.
- Les annotations sont incrustées dans le PDF sous forme d'image (toutes les langues sont conservées). Les notes sont des annotations.

## 13. Fichiers de travail (.pdfkobo)
- [Enregistrer] (Ctrl+S) crée un fichier .pdfkobo. Ouvrez-le avec [Ouvrir] ou par glisser-déposer pour reprendre avec pages, annotations, tampons, notes et filigrane modifiables. Vous pouvez le transmettre à un collègue qui suivra les consignes des notes.
- Attention : le fichier de travail contient le PDF d'origine tel quel, y compris le texte sous les masques. Ne le donnez pas à l'extérieur de votre organisation ; partagez plutôt le PDF exporté.
- Le carnet de tampons et l'historique d'annulation ne sont pas inclus. Les modifications non enregistrées affichent « * » dans le titre et déclenchent un avertissement à la fermeture.

## 14. Affichage et réglages
- Zoom : Page entière / Largeur de page / 25–400 %, Ctrl+molette, Ctrl++ / Ctrl+−, Ctrl+0 pour la page entière.
- Miniatures : curseur Taille, Colonnes (Auto / 1–6), Ctrl+molette.
- Thèmes : Moderne / Sombre / PC rétro / Aqua / Console. Langues : 日本語, English, 简体中文, 繁體中文, Português, Français, 한국어. Les deux sont mémorisés.

## 15. Raccourcis clavier
- Ctrl+O ouvrir / Ctrl+S enregistrer / Ctrl+Z annuler / Ctrl+Y ou Ctrl+Maj+Z rétablir / Ctrl+F rechercher / F3 ou Entrée résultat suivant / Maj+Entrée précédent
- Suppr : supprimer l'annotation sélectionnée (les pages quand les miniatures ont le focus) / flèches : ajuster (Maj = plus grand) / Échap : désélectionner → outil Sélection
- PageUp / PageDown changer de page / Ctrl+A toutes les miniatures (tout le texte en Sél. texte) / Ctrl+C copier le texte sélectionné / Ctrl+V coller image ou texte
- Ctrl+molette, Ctrl++ / −, Ctrl+0 zoom / Ctrl+Entrée valider la saisie d'une note

## 16. Diffusion et dépannage
- La messagerie de l'entreprise peut bloquer les pièces jointes .html → envoyez un ZIP ou utilisez un dossier partagé / Teams.
- L'ouverture directe depuis l'aperçu d'un e-mail ou du cloud impose des restrictions (carnet non mémorisé, pas de boîte d'enregistrement, pas de presse-papiers) → enregistrez d'abord le fichier sur le PC puis double-cliquez dessus.
- Carnet, thème, langue, auteur des notes, etc. sont stockés dans le navigateur de chaque PC (localStorage, préfixe pdfkobo98.). Effacer les données du navigateur les supprime : sauvegardez le carnet.
- Non pris en charge : modification du texte existant du PDF, vrai caviardage (suppression dans la structure du PDF ; utilisez la conversion de page en image), OCR, signatures numériques, création de formulaires.

## 17. Licence, droits d'auteur et source officielle
- Copyright © 2026 Front Softworks. Licence : MIT License (texte complet dans l'application via [ⓘ] → Licence MIT, et dans le fichier LICENSE).
- Selon la MIT License, tout particulier ou entreprise peut utiliser, copier, modifier, redistribuer et exploiter commercialement le logiciel gratuitement. La seule condition est de conserver la mention de copyright et le texte de la licence.
- Aucune garantie : le logiciel est fourni « en l'état » et l'auteur n'assume aucune garantie ni responsabilité. Vérifiez toujours le résultat exporté des documents importants.
- Logiciels inclus : PDF.js (Apache License 2.0) ; pdf-lib, pako, @pdf-lib/standard-fonts, @pdf-lib/upng, qrcode-generator (MIT) ; tslib (0BSD) ; CMaps Adobe (BSD-3-Clause) ; PDFium JBIG2 (BSD-3-Clause) ; OpenJPEG (BSD-2-Clause). Textes des licences : [ⓘ] → Licences tierces, et THIRD_PARTY_NOTICES.txt.
- Source officielle : la page des versions sur GitHub (l'URL est affichée dans [ⓘ]). Les fichiers obtenus ailleurs peuvent avoir été modifiés ; l'auteur n'est pas responsable des problèmes causés par des versions modifiées.
- L'auteur ne distribue jamais le logiciel par e-mail. Pour le recommander, partagez l'URL de la source officielle plutôt que le fichier ([ⓘ] → « Copier le texte et l'URL »). L'écran d'accueil au premier lancement affiche aussi la source officielle.
- Les PDF exportés portent « Front PDF v1.0.1 (Front Softworks) » et l'URL officielle dans leurs propriétés (Producer/Creator).
- À la première utilisation, une activation gratuite est nécessaire (une fois par navigateur) : (1) copiez « l'ID de ce navigateur » affiché (8 caractères aléatoires créés par l'app ; aucune information sur le PC ou personnelle), collez-le dans « Activation » sur la page officielle et cliquez sur « Émettre » ; (2) collez dans l'app le mot de passe affiché (ou le mot de passe court à 10 caractères). Scanner le QR code avec un téléphone ouvre la page officielle avec l'ID déjà rempli. Le mot de passe ne fonctionne que dans ce navigateur, pas sur d'autres PC ou navigateurs. La page officielle n'envoie pas l'ID ; le calcul se fait dans le navigateur. Effacer les données du navigateur change l'ID : activez à nouveau. L'ID peut être copié à tout moment tant que cet écran est ouvert (il ne peut pas être fermé).
- Autres logiciels de Front Softworks : ExVAN Planner (optimiseur de chargement de conteneurs, https://exvan-planner.github.io/).
- Vérifier que le fichier n'a pas été modifié (Windows, rien à installer) : exécutez `certutil -hashfile Front_PDF.html SHA256` dans l'invite de commandes et vérifiez que la valeur correspond au SHA-256 publié sur la source officielle.
