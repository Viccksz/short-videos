# Protocolo de Auto-Inspeção Visual pelo Agente (Hard Gate)

## O Princípio do Portão de Qualidade
O usuário não deve ser surpreendido com anomalias grotescas no vídeo final (ex: estilo 3D brilhante no meio de ilustrações em papel kraft, pessoas sentadas escrevendo em mesas quando o roteiro falava de contemplar a janela, ou mãos com 6 dedos).

A responsabilidade de auditar e aprovar cada quadro gerado é **do próprio agente, de forma 100% autônoma**.

---

## 🛑 Regra de Ouro Inviolável
> **Nenhum arquivo de imagem pode ser incluído no script de montagem do vídeo (`build_video.py` ou comando FFmpeg) sem que o agente tenha inspecionado visualmente o seu conteúdo.**

---

## 🔍 Checklist de Inspeção por Imagem
Ao gerar cada uma das 10 imagens, o agente deve rodar uma rotina de verificação:

1. **Checagem de Estilo Artístico:**
   - A imagem tem textura orgânica de papel kraft e giz pastel oleoso/lápis de cor?
   - Ou parece um render digital suave, filtro 3D, CGI ou anime comercial brilhante?
   - *Se parecer arte digital lisa:* **REPROVADA.** Descarte o arquivo imediatamente.

2. **Checagem de Fidelidade Narrativa (Roteiro):**
   - O que está desenhado na imagem é exatamente o que a tela do roteiro pediu?
   - Exemplo de falha: O roteiro pede "rapaz sentado na beira da cama esfregando os olhos", mas a IA gerou "uma pessoa sentada numa escrivaninha escrevendo em um caderno com caneta".
   - *Se houver divergência de enredo:* **REPROVADA.** Descarte o arquivo.

3. **Checagem da Ficha de Personagem (Se houver personagem):**
   - A idade aparenta ter 20 anos?
   - O corte de cabelo é consistente?
   - As roupas são as cravadas na ficha (camiseta cinza mescla waffle knit)?
   - *Se virar criança, idoso ou mudar de roupa:* **REPROVADA.** Descarte o arquivo.

4. **Checagem de Anatomia e Artefatos:**
   - Mãos estranhas, membros duplicados, olhos deformados ou textos ilegíveis gerados pela IA.
   - *Se houver anomalia visual grotesca:* **REPROVADA.** Descarte o arquivo.

---

## 🗑️ Política de Quarentena e Descarte Imediato
Quando uma imagem for reprovada na inspeção:
1. **Nunca deixe o arquivo solto na pasta principal** com nome genérico.
2. Mova o arquivo reprovado para uma pasta `scratch/rejeitados/` ou delete-o imediatamente.
3. Isso impede que na hora de escrever o script de montagem (OpenCV/FFmpeg) o agente pegue por engano um arquivo descartado para preencher a linha do tempo.

---

## 🔄 Procedimento em Caso de Falha de Cota (HTTP 429)
Se a cota do modelo generativo for atingida durante o processo:
* **NUNCA:** Nunca pegue um arquivo defeituoso antigo descartado para "tapar buraco" na linha do tempo.
* **SEMPRE:**
  1. Verifique se há uma imagem de arquivo autêntica já aprovada em sessões anteriores que sirva harmonicamente para a cena (ex: mãos segurando caneca em papel kraft).
  2. Ou utilize movimentos de câmera inteligentes sobre cenas já aprovadas (ex: um recorte cinematográfico e pan lento sobre o ambiente do quarto ou janela matinal).
  3. Comunique com total transparência a situação.
