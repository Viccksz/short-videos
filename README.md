# 🎬 short-videos (Antigravity Skill)

Skill para o **Google Antigravity** projetada para criar vídeos curtos, dinâmicos e autorais para **Reels, TikTok e Shorts (1080x1920, 9:16)**, com controle milimétrico de roteiro, consistência visual, áudio harmonioso e renderização procedural.

---

## 🌟 Pilares do Workflow

1. **Roteiro e Decupagem em 10 Telas Dinâmicas:**  
   O tempo total do vídeo ($T$) é dividido obrigatoriamente por 10 ($\Delta t = T / 10$). Cada tela dura $T / 10$ (ex: 30s = 3s/tela; 40s = 4s/tela), garantindo ritmo visual ágil sem telas estáticas.
2. **Áudio Flexível & Fim do Corte Seco:**  
   Suporta narração por voz (ElevenLabs / TTS), música instrumental ambiente, ambos com ducking automático ou mudo. O Quadro 10 possui respiro obrigatório de 1.5s a 2.0s e fade out suave conjunto de áudio e vídeo para o preto.
3. **Trava Rígida de Personagem & Estilo:**  
   Ficha de personagem (*Character Sheet*) travada (idade exata, corte de cabelo, vestuário fixo) para impedir discrepâncias entre quadros.
4. **Auto-Inspeção Visual Autônoma (Hard Gate):**  
   O agente é obrigado a inspecionar visualmente cada um dos 10 quadros gerados antes de mandar para o FFmpeg. Imagens com estilo anime/3D errado ou alucinações são descartadas e regeradas autonomamente.
5. **Render Procedural de Câmera & Textura:**  
   Movimentos de câmera suaves (*push-in, pan, sway*), partículas de poeira luminosa e transições *dissolve* cinematográficas de 4 frames.

---

## 📁 Estrutura de Arquivos

```
short-videos/
├── SKILL.md                                 # Manual mestre e prompt da skill
├── README.md                                # Documentação do repositório
├── .gitignore                               # Filtros de arquivos temporários
├── references/
│   ├── roteiro-e-tempo.md                   # Fórmulas de timing e decupagem das 10 telas
│   ├── estilos-e-prompts.md                 # Presets de estilos artísticos e prompts
│   ├── personagem-e-continuidade.md         # Template de Character Sheet e regras
│   ├── inspecao-e-qualidade.md              # Protocolo de auto-inspeção visual do agente
│   └── audio-e-sincronismo.md               # Padrões de áudio, ducking e fade out
└── scripts/
    ├── generate_audio.py                    # Gerador de TTS auxiliar via EdgeTTS
    ├── render_short_video.py                # Motor de animação e mux em OpenCV + FFmpeg
    └── verify_video.py                      # Validador técnico de vídeo via ffprobe
```

---

## 🚀 Como Instalar e Usar no Antigravity

Clone este repositório na sua pasta de skills globais do Antigravity:

```bash
cd ~/.gemini/config/skills/
git clone https://github.com/Viccksz/short-videos.git
```

No chat com o Antigravity, basta pedir:
> *"Quero criar um vídeo curto sobre desaceleração matinal de 30 segundos no estilo kraft com música e narração."*

O agente ativará a skill `/short-videos` e executará todas as etapas com inspeção visual garantida.
