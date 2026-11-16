# Personagem e Continuidade Visual

## O Problema Clássico da IA em Vídeos Sequenciais
Modelos generativos de imagem tendem a variar drasticamente traços entre um quadro e outro se as instruções deixarem margem para interpretação:
* Em uma cena o personagem parece uma criança de 10 anos; na outra, um homem de 35 anos.
* Em uma cena ele veste suéter grosso de gola alta; na outra, uma camiseta branca lisa.
* Os traços faciais mudam de formato e etnia.

Para eliminar 100% esse problema, a skill estabelece **três travas inegociáveis**.

---

## 🔒 As 3 Travas de Continuidade

### 1. Ficha de Personagem (Character Sheet) Fixa
Antes de gerar qualquer imagem em que o personagem apareça de corpo inteiro ou rosto, preencha e trave os dados:

```yaml
personagem:
  idade: "20 anos (jovem adulto universitário/profissional, proporção cabeça/corpo 1:7.5, biótipo esguio normal)"
  rosto: "Cabelo castanho escuro curto e ondulado, rosto jovem sem barba, traços suaves mas claramente adultos"
  vestuario_superior: "Camiseta de manga longa cinza mescla em malha waffle (heather-grey waffle-knit)"
  vestuario_inferior: "Calça comprida azul-marinho escura em algodão rústico"
  calcados: "Descalço (em casa) ou meias de lã crua"
```

> [!WARNING]
> **Termos proibidos no prompt:** Nunca use "boy", "kid", "little boy", "menino" ou "garoto". Essas palavras disparam alucinações de idade infantil no modelo generativo. Use sempre: `20-year-old young adult male` ou `slender 20-year-old young man`.

---

### 2. Estratégia de Decupagem Inteligente (Planos de Detalhe)
Em um vídeo de 10 telas, o rosto/corpo completo do protagonista **NÃO deve aparecer em todas as 10 cenas**:
* **Apenas 2 a 3 cenas com rosto/corpo:** (ex: Tela 04 acordando, Tela 06 preparando algo, Tela 10 na janela).
* **As outras 7 a 8 cenas focam em detalhes sensoriais e ambiente:**
  * Mão pegando um objeto (detalhe do pulso com a manga cinza mescla waffle).
  * Pés descalços no piso de madeira.
  * O smartphone na mesa de madeira.
  * Macro da xícara e do vapor em contraluz.
  * O quarto em penumbra ou a janela.

Isso cumpre dois objetivos fundamentais ao mesmo tempo:
1. Deixa o vídeo muito mais cinematográfico, poético e sensorial (linguagem de cinema de autor).
2. Reduz o risco de discrepâncias faciais a quase zero, pois o rosto só é visto em momentos-chave calculados.

---

### 3. Trava de Vestuário em Planos de Detalhe
Mesmo nos planos de detalhe (como as mãos segurando uma caneca ou pegando o celular), o vestuário deve ser mantido consistente no prompt:
> `Close-up shot of the hands of the 20-year-old young man, ribbed cuffs of his heather-grey waffle-knit long-sleeve shirt visible at the wrists, gently holding...`
