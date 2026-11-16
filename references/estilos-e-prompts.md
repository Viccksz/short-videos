# Estilos Visuais e Fórmulas de Prompts

## 🎨 Presets de Estilo

### Estilo 1: Artesanal Europeu em Papel Kraft (Padrão)
* **Essência:** Traço autoral de livro ilustrado europeu contemporâneo (*indie storybook illustration*), feito com lápis de cor, giz pastel oleoso e giz de cera sobre papel kraft pardo rústico com granulação orgânica e hachuras finas.
* **Paleta de Cores:** Tons terrosos quentes: mostarda, âmbar dourado, azul-marinho profundo, terracota, creme e marrom kraft.
* **Palavras-chave obrigatórias no prompt:**
  > `masterpiece, European artisanal indie book illustration, hand-drawn colored pencil and rich oil pastel texture on raw brown textured kraft paper, visible organic fibrous paper grain, delicate pencil cross-hatching, warm earthy color palette, muted ochre, burnt terracotta, deep navy blue, soft warm ambient lighting, cozy tactile atmosphere, vertical 9:16 aspect ratio`
* **Proibido no negativo:** `anime, glossy 3D, CGI render, digital airbrush, smooth plastic skin, neon colors, photographic realism, saturated gradient, sparkles, modern vector flat art`.

---

### Estilo 2: Aquarela Editorial Minimalista
* **Essência:** Ilustração editorial sofisticada em aquarela molhada sobre papel algodão prensado a frio (*cold-press cotton paper*), com manchas orgânicas de tinta (*watercolor bleeds*), linhas de nanquim preto fino e espaços negativos respirados.
* **Paleta de Cores:** Lavadas translúcidas de verde sálvia, azul petróleo, ocre e cinza quente.
* **Palavras-chave obrigatórias:**
  > `masterpiece, editorial watercolor illustration, expressive wet-on-wet watercolor washes, delicate fine black ink contour linework, textured heavy cold-pressed cotton paper with rough organic grain, natural pigment granulation, minimalist poetic composition, tranquil muted tones of sage green, slate blue, and warm sand, vertical 9:16 aspect ratio`
* **Proibido no negativo:** `oil pastel, digital shiny art, hyperrealistic photo, saturated plastic, 3D CGI`.

---

### Estilo 3: Lofi & Studio Ghibli Aconchegante
* **Essência:** Pintura de fundo artesanal tradicional em guache (*anime background painting*), cenários bucólicos e iluminados com sensação nostálgica e aconchegante.
* **Paleta de Cores:** Verdes exuberantes, azul céu suave, luz solar matinal filtrada (*komorebi*) e sombras azuladas suaves.
* **Palavras-chave obrigatórias:**
  > `masterpiece, classic anime background art style, traditional gouache painting, Studio Ghibli aesthetic, cozy peaceful atmosphere, soft dappled morning sunlight filtering through leaves, warm nostalgic colors, detailed painterly brushwork, vertical 9:16 aspect ratio`
* **Proibido no negativo:** `glossy 3D, dark gritty noir, oversaturated CGI, digital vectors`.

---

## 📐 Estrutura Padrão de Prompt para Geração de Imagem

Monte os prompts em inglês seguindo esta ordem rigorosa de blocos:

```
[BLOCO 1: IDENTIDADE DE ESTILO]
"masterpiece, European artisanal indie book illustration, hand-drawn colored pencil and oil pastel on textured brown kraft paper..."

[BLOCO 2: PLANO E COMPOSIÇÃO]
"Vertical 9:16 aspect ratio, close-up macro shot / medium cinematic shot of..."

[BLOCO 3: ASSUNTO E AÇÃO ESPECÍFICA]
"A 20-year-old young man with short wavy dark brown hair, wearing a loose heather-grey waffle-knit long-sleeve shirt, gently holding..."

[BLOCO 4: CENÁRIO E ILUMINAÇÃO]
"In a quiet rustic wooden kitchen, soft morning sunlight casting long golden shadows and highlighting delicate steam..."

[BLOCO 5: CLIMA EMOCIONAL E TEXTURA]
"Deeply peaceful, slow living, tactile texture, visible fibrous paper grain, muted earthy tones."
```

---

## 🛡️ Uso de Imagens de Referência (`ImagePaths`)
Ao gerar cenas com o mesmo personagem ou ambiente consecutivo:
1. Passe o primeiro quadro aprovado como referência (`ImagePaths`).
2. Mantenha no prompt os mesmos adjetivos descritivos exatos de roupas e cabelo.
3. Se a IA errar ou ignorar o estilo, gere em modo texto puro com ênfase redobrada nos materiais tradicionais (`traditional oil pastel on brown kraft paper, NO DIGITAL GLOSS`).
