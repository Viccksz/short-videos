# Roteiro e Decupagem das 10 Telas

## A Regra dos 10 Quadros
Para vídeos de redes sociais (Reels, TikTok, Shorts), uma tela estática por mais de 3 ou 4 segundos perde a retenção do espectador. Por isso, a regra padrão da skill é **sempre dividir a duração total por 10 telas dinâmicas**.

### Fórmula de Cálculo:
$$\text{Duração por Tela } (\Delta t) = \frac{\text{Tempo Total } (T)}{10}$$

| Tempo Total ($T$) | Duração por Tela ($\Delta t$) | Total de Quadros a 24 FPS |
|---|---|---|
| **20 segundos** | 2.0 segundos | 48 frames por tela |
| **30 segundos** | 3.0 segundos | 72 frames por tela |
| **40 segundos** | 4.0 segundos | 96 frames por tela |
| **60 segundos** | 6.0 segundos | 144 frames por tela |

*Observação:* Quando houver narração por voz, a duração da narração real determina a base do tempo total (ver `references/audio-e-sincronismo.md`).

---

## Estrutura de Alternância de Planos (Ritmo Visual)
Para um vídeo de 10 telas prender a atenção sem parecer uma colagem aleatória, utilize a decupagem em 3 atos:

### Ato 1: Gancho e Contexto (Telas 01 a 03)
* **Tela 01 (Ambiente/Abertura):** Plano geral aconchegante ou em penumbra estabelecendo o clima.
* **Tela 02 (Ação Inicial / Conflito):** Plano médio ou detalhe da ação cotidiana (ex: mão no despertador, mão pegando o celular, xícara fria).
* **Tela 03 (Macro Emocional):** Super close-up (ex: tela cheia de notificações, olhar perdido, relógio correndo).

### Ato 2: Ruptura e Mudança de Consciência (Telas 04 a 07)
* **Tela 04 (Expressão do Personagem):** O protagonista reage ou percebe o momento (ex: sentando na cama esfregando os olhos, respirando fundo).
* **Tela 05 (Detalhe Sensorial Terrestre):** Elemento físico e tátil (ex: pés descalços no piso de madeira, água caindo na pia).
* **Tela 06 (Ação de Presença):** O protagonista realizando algo simples e manual (ex: passando café, molhando uma planta, abrindo a cortina).
* **Tela 07 (Macro Poético):** Elemento atmosférico em destaque (ex: vapor da bebida em contraluz com o sol, poeira luminosa, chuva na vidraça).

### Ato 3: Conclusão e Respiro (Telas 08 a 10)
* **Tela 08 (Desconexão / Escolha):** Detalhe da decisão (ex: celular virado para baixo na mesa, livro aberto).
* **Tela 09 (Sensação de Conforto):** Plano detalhe acolhedor (ex: mãos envolvendo a caneca quente, fones de ouvido nos ouvidos).
* **Tela 10 (Fechamento e Janela):** Plano aberto ou contemplativo (ex: janela aberta com a luz do dia, horizonte em paz). É a tela que ancora a mensagem final e recebe o respiro de 1.5s a 2s antes do fade out.

---

## Modelo de Tabela de Storyboard para Apresentar ao Usuário

Antes de gerar qualquer arte, apresente a tabela no seguinte formato:

```markdown
| # | Janela de Tempo | Descrição Visual da Cena | Tipo de Plano | Narração Sincronizada | Movimento de Câmera |
|---|---|---|---|---|---|
| **01** | `00.0s – 03.0s` | Quarto rústico em penumbra matinal | Plano Geral | "Você mal abriu os olhos..." | Slow Push-in lento |
| **02** | `03.0s – 06.0s` | Mão alcançando o celular sob o travesseiro | Plano Detalhe | "...e já carregou o peso do mundo..." | Pan descendente suave |
...
| **10** | `27.0s – 33.0s` | Janela banhada pela luz dourada da aurora | Contemplativo | "Começa aqui dentro." (silêncio final) | Sway suave + Fade out |
```
