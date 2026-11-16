---
name: short-videos
description: Cria vídeos curtos e dinâmicos para Reels, TikTok e Shorts (1080x1920, 9:16), dividindo o tempo escolhido por 10 telas (~3s por tela) com movimentos de câmera, estilo consistente, narração/música flexível, auto-inspeção visual de cada imagem e finalização com fade suave sem corte abrupto. Use quando o usuário pedir para criar vídeo curto, vídeo animado, reel, shorts, vídeo reflexivo ou transformar um roteiro em vídeo.
---

# /short-videos

Workflow completo para produzir vídeos curtos, dinâmicos e autorais com controle milimétrico de roteiro, consistência visual e áudio harmonioso.

A qualidade e a consistência deste pipeline vêm de **cinco pilares fundamentais**:
1. **Roteiro e Decupagem em 10 Telas**: O tempo total do vídeo ($T$) é dividido obrigatoriamente por 10. Cada tela dura $T / 10$, garantindo dinamismo visual sem ficar estático.
2. **Áudio Flexível e Sem Corte Seco**: O usuário escolhe entre narração (voz TTS humana), música de fundo, ambos combinados (com ducking automático) ou mudo. A música e o vídeo **nunca terminam de repente** — há respiro de 1.5s a 2.0s e fade out obrigatório.
3. **Trava Rígida de Personagem e Estilo**: Se houver protagonista, idade, roupas e traços são cravados no início para impedir discrepâncias de idade ou vestuário.
4. **Auto-Inspeção Visual pelo Agente (Hard Gate)**: O próprio agente deve inspecionar cada um dos 10 quadros gerados antes de mandar para o FFmpeg. Imagens com estilo anime/3D errado ou alucinações são descartadas e regeradas autonomamente.
5. **Render Procedural de Câmera e Partículas**: Movimentos suaves (push-in, pan, sway), partículas de poeira luminosa e transições dissolve cinematográficas de 4 frames.

---

## 🧭 As 6 Fases do Workflow

### Fase 0: Coleta de Parâmetros e Alinhamento
Pergunte ou confirme com o usuário:
1. **Roteiro / Tema**: O usuário fornece o texto ou pede opções temáticas.
2. **Tempo Total ($T$)**: Ex: 30s, 40s, 60s. O padrão sugerido é 30 segundos.
   - Cálculo automático dos 10 quadros: $\text{Duração por tela} = T / 10$ (ex: 30s $\rightarrow$ 3.0s por tela).
3. **Configuração de Áudio**:
   - `1`: Narração + Música de fundo com ducking (Padrão mais imersivo).
   - `2`: Apenas Narração.
   - `3`: Apenas Música instrumental.
   - `4`: Mudo (Sem áudio).
4. **Estilo Visual**:
   - *Estilo 1 (Padrão)*: Giz pastel oleoso e lápis de cor sobre papel kraft rústico (artesanal europeu).
   - *Estilo 2*: Aquarela editorial minimalista sobre papel texturizado.
   - *Estilo 3*: Lofi / animação acolhedora estilo Studio Ghibli.
   - *Estilo Personalizado*: O usuário define os elementos de direção de arte.
5. **Personagem**:
   - Tem protagonista? Se sim, preencher imediatamente a **Ficha de Personagem** (Fase 2). Se for vídeo conceitual/abstrato/objetos, pular a ficha.

---

### Fase 1: Roteiro e Decupagem das 10 Telas
Consulte `references/roteiro-e-tempo.md`.
- Escreva a tabela de decupagem com exatamente **10 telas**.
- Alterne o tipo de plano para criar ritmo:
  - Planos de abertura/ambiente (quarto, janela, rua).
  - Planos de detalhe/macro sensoriais (mãos, vapor, pés, celular, objetos).
  - Planos de expressão/personagem (se houver protagonista).
- O roteiro é apresentado e aprovado antes de gerar qualquer imagem.

---

### Fase 2: Trava de Personagem e Continuidade (Se houver)
Consulte `references/personagem-e-continuidade.md`.
Para evitar que o personagem mude de idade ou roupa entre telas:
1. **Idade Fixa**: Cravar em anos (ex: "Jovem adulto de 20 anos, 1.75m, proporções corporais adultas normais"). Proibido usar termos ambíguos como "menino" ou "garoto" que a IA possa interpretar como criança em um quadro e adulto em outro.
2. **Vestuário Travado**: Nomear tecidos e cores específicas (ex: "Camiseta de manga longa cinza mescla em malha waffle, calça escura de algodão").
3. **Referência Cruzada**: O primeiro quadro aprovado do personagem vira `ImagePaths` de referência para todos os próximos quadros em que ele aparecer.

---

### Fase 3: Checagem de Cotas & Geração de Imagens
Consulte `references/estilos-e-prompts.md`.
- Antes de iniciar a esteira, valide se o modelo de imagem possui cotas disponíveis.
- Gerar os quadros em lotes lógicos (ex: Telas 01 a 05, depois 06 a 10).
- Aspect ratio obrigatório: `9:16` vertical (`768x1376` ou `1080x1920`).

---

### Fase 4: Auto-Inspeção Visual pelo Agente (Hard Gate Obrigatório)
Consulte `references/inspecao-e-qualidade.md`.
> [!IMPORTANT]
> **REGRA DE OURO INVIOLÁVEL:** O agente é terminantemente proibido de adicionar um arquivo à linha do tempo sem antes abrir e verificar o que está desenhado nele.

Checklist interno que o agente deve validar para cada uma das 10 imagens:
- [ ] O estilo é fiel à direção de arte (ex: textura kraft visível, sem cara de anime 3D ou render liso)?
- [ ] Se tiver personagem, a idade e as roupas batem com a Ficha de Personagem?
- [ ] A cena ilustra o que o roteiro daquela tela pede?
- [ ] Não há alucinações (membros extras, objetos anacrônicos, pessoas escrevendo quando deveriam olhar a janela)?

**Se qualquer imagem falhar:** O agente descarta o arquivo com defeito, ajusta o prompt e regera até aprovar. NUNCA reaproveite arquivos defeituosos descartados de outras tentativas.

---

### Fase 5: Áudio e Sincronismo (Fim do Corte Seco)
Consulte `references/audio-e-sincronismo.md`.
1. **Duração guiada pelo áudio**: Se a narração levar 32 segundos, o tempo total do vídeo é ajustado para `32s + 2s de respiro = 34s`. As 10 telas duram `3.4s` cada.
2. **Buffer de Respiro no Quadro 10**: Os últimos 1.5s a 2.0s do Quadro 10 permanecem sem narração, deixando apenas a música tocar suavemente antes de terminar.
3. **Fade Out Obrigatório**:
   - Áudio: `afade=t=out:st=<FIM-2s>:d=2.0` na música.
   - Vídeo: Fade suave para o preto nos últimos 24 quadros (1 segundo).
   - Proibido qualquer áudio ou vídeo cortar de repente.

---

### Fase 6: Renderização e Verificação Técnica
Use o script padrão da skill `scripts/render_short_video.py` ou monte a pipeline com OpenCV + FFmpeg:
- Resolução de saída: `1080x1920` (9:16 vertical).
- Taxa de quadros: `24 FPS`.
- Codec: H.264 High Profile (`libx264`, `pix_fmt yuv420p`, CRF 18).
- Áudio: AAC 256k estéreo.
- Executar `scripts/verify_video.py` via `ffprobe` para garantir duração, ausência de quedas e integridade do arquivo.

---

## 📁 Estrutura de Arquivos da Skill

- `SKILL.md`: Guia mestre do workflow (este arquivo).
- `references/roteiro-e-tempo.md`: Fórmulas de cálculo de tempo, estrutura das 10 telas e dinâmica de corte.
- `references/estilos-e-prompts.md`: Fórmulas de prompts e presets de estilos visuais.
- `references/personagem-e-continuidade.md`: Template de Character Sheet e regras de consistência.
- `references/inspecao-e-qualidade.md`: Protocolo de auto-inspeção visual para barrar alucinações.
- `references/audio-e-sincronismo.md`: Padrão de geração TTS, trilha ambiente, ducking e fade out.
- `scripts/render_short_video.py`: Script modular em Python para montagem de câmeras, partículas e mux de áudio.
- `scripts/generate_audio.py`: Script auxiliar de TTS via EdgeTTS com vozes naturais em português.
- `scripts/verify_video.py`: Script de validação automática do MP4 gerado.
