# Áudio, Narração e Sincronismo (Fim do Corte Seco)

## Política de Áudio da Skill

A experiência sensorial de um vídeo curto depende 50% da qualidade sonora. Vídeos em que a voz termina no meio da palavra, o som acaba "do nada" com um corte abrupto ou a música afoga a fala são inaceitáveis.

---

## 🎚️ As 4 Regras de Ouro do Áudio

### 1. A Narração Guia o Relógio do Vídeo
Se o usuário escolheu narração por voz (TTS):
* Gere primeiro todos os blocos de áudio da narração.
* Meça a duração real de cada fala com `ffprobe` ou biblioteca de áudio.
* Calcule a duração total mínima necessária:
  $$\text{Duração Total do Vídeo } (T) = \text{Duração da Narração} + 1.8\text{ segundos de respiro}$$
* Em seguida, recalcule a duração de cada uma das 10 telas:
  $$\Delta t = \frac{T}{10}$$
* **Resultado:** O vídeo nunca acaba antes da voz terminar de falar.

---

### 2. O Buffer de Respiro no Quadro 10
A última frase de um vídeo reflexivo carrega a moral da história (o fechamento poético).
* A narração deve encerrar **antes** do final do vídeo.
* Deixe obrigatoriamente **entre 1.5 e 2.0 segundos de silêncio na voz** após a última palavra, deixando apenas a trilha sonora tocar suavemente.
* Isso permite que a mensagem assente no espectador antes do vídeo reiniciar ou ir para o próximo post.

---

### 3. Fade Out Obrigatório (Sem Cortes Abruptos)
É expressamente proibido cortar áudio a seco no final do vídeo.
* **Filtro de Fade Out no FFmpeg:**
  ```
  afade=t=out:st=<TEMPO_INICIO_FADE>:d=2.0
  ```
  *(Onde `TEMPO_INICIO_FADE` é a duração total menos 2 segundos).*
* O fade de áudio deve ser sincronizado com o fade visual para o preto nos últimos 24 quadros (1 segundo) do vídeo.

---

### 4. Ducking Automático da Trilha Sonora
Quando o vídeo tiver **Narração + Trilha de Fundo**:
* A trilha instrumental deve ficar em volume reduzido (entre 18% e 25% do volume original) sob a voz para garantir inteligibilidade absoluta da fala.
* Nos segundos finais (durante o respiro do Quadro 10), a música pode subir suavemente antes de fazer o fade out final.
* Exemplo de filter_complex no FFmpeg:
  ```
  [1:a]volume=1.25[voz];
  [2:a]volume=0.22,afade=t=out:st=31.5:d=2.0[musica];
  [voz][musica]amix=inputs=2:duration=longest:dropout_transition=0[aout]
  ```

---

## 🎙️ Geração de Narração com EdgeTTS
Voz recomendada para narrações intimistas e reflexivas em português do Brasil:
* **Voz:** `pt-BR-AntonioNeural` (masculina calma e profunda) ou `pt-BR-FranciscaNeural` (feminina expressiva e acolhedora).
* **Ajuste de Cadência:** `rate="-4%"` a `"-6%"` (ritmo levemente desacelerado para soar reflexivo, não corrido).
* **Ajuste de Tom:** `pitch="-1Hz"` (tom ligeiramente encorpado e sereno).
