# DevMobile: Desenvolvimento de Aplicativos Mobile

Material de estudo em **slides Beamer (LaTeX)** no modelo da casa (azul-petróleo e âmbar), organizado em **15 módulos independentes**, que vai do ecossistema mobile até a publicação na Google Play, com IoT (ESP32 via BLE e MQTT), multiplataforma e IA no dispositivo.

A stack principal é **Kotlin + Jetpack Compose**, com a arquitetura recomendada pelo Google (MVVM, repositórios e Hilt), Room, Retrofit e Firebase. Um projeto integrador, o **LabMonitor** (um app para laboratórios de eletroeletrônica), evolui ao longo de todos os módulos.

> Os PDFs compilados ficam na pasta [`pdf/`](pdf/).

## Módulos

| Nº | Módulo | Conteúdo principal | Slides |
|----|--------|--------------------|-------:|
| 00 | [Apresentação e Ecossistema Mobile](modulos/modulo00-apresentacao.tex) | abordagens (nativa, multiplataforma, híbrida, PWA), arquitetura do Android, níveis de API, stack do curso | 27 |
| 01 | [Ambiente de Desenvolvimento](modulos/modulo01-ambiente.tex) | Android Studio, emulador, celular real, ADB, estrutura do projeto, Gradle, Git | 30 |
| 02 | [Kotlin Essencial](modulos/modulo02-kotlin.tex) | tipos, null safety, funções e lambdas, OO, `data`/`sealed`, coleções, funções de escopo | 30 |
| 03 | [Kotlin Assíncrono: Coroutines e Flow](modulos/modulo03-coroutines.tex) | thread principal, `suspend`, dispatchers, concorrência estruturada, Flow, StateFlow | 25 |
| 04 | [Interfaces com Jetpack Compose](modulos/modulo04-compose.tex) | UI declarativa, componentes, layouts, modifiers, listas, Material 3 e temas | 25 |
| 05 | [Estado e Navegação](modulos/modulo05-estado-navegacao.tex) | `remember`, state hoisting, efeitos, ciclo de vida, **Navigation 3** | 25 |
| 06 | [Arquitetura de Apps](modulos/modulo06-arquitetura.tex) | camadas, MVVM, UiState, repositórios, casos de uso, Hilt | 27 |
| 07 | [Persistência Local](modulos/modulo07-persistencia.tex) | DataStore, Room, relações, migrações | 23 |
| 08 | [Rede e Consumo de APIs](modulos/modulo08-rede-apis.tex) | HTTP/REST, Retrofit, OkHttp, erros, offline-first, segurança | 28 |
| 09 | [Firebase](modulos/modulo09-firebase.tex) | Auth, Firestore, regras de segurança, Storage, FCM, Crashlytics | 26 |
| 10 | [Recursos do Dispositivo e IoT](modulos/modulo10-dispositivo-iot.tex) | permissões, QR code, WorkManager, sensores, **BLE com ESP32**, **MQTT** | 29 |
| 11 | [Testes e Qualidade](modulos/modulo11-testes-qualidade.tex) | testes unitários e de UI, Turbine, MockK, desempenho, acessibilidade, CI | 24 |
| 12 | [Publicação na Google Play](modulos/modulo12-publicacao.tex) | release, assinatura, Play Console, testes fechados, verificação de desenvolvedor, LGPD | 26 |
| 13 | [Desenvolvimento Multiplataforma](modulos/modulo13-multiplataforma.tex) | Flutter, React Native, Kotlin Multiplatform | 23 |
| 14 | [Tópicos Avançados e Projeto Final](modulos/modulo14-avancados-projeto.tex) | IA (LiteRT, ML Kit, Firebase AI Logic), segurança (MASVS), monetização, projeto final | 22 |

Cada módulo traz objetivos, roteiro, teoria com diagramas em TikZ, código comentado, resumo, exercícios, a etapa correspondente do projeto LabMonitor e referências oficiais.

## Estrutura do repositório

```
DevMobile/
├── estilo/
│   └── devmobile.sty          # modelo da casa: cores, capa, seções, caixas, código, TikZ
├── modulos/
│   ├── modulo00-apresentacao.tex
│   ├── ...
│   └── modulo14-avancados-projeto.tex
├── pdf/                       # PDFs compilados
├── ferramentas/
│   └── verificar_layout.py    # checa erros, overfull boxes e slides transbordando
├── Makefile
└── .github/workflows/slides.yml   # compila todos os módulos a cada push
```

## Como compilar

Requisitos: TeX Live com `beamer`, `tcolorbox`, `listings`, `pgf/tikz` e `babel-portuguese` (no Debian/Ubuntu: `texlive-latex-extra`, `texlive-pictures` e `texlive-lang-portuguese`).

```bash
make              # compila todos os módulos e copia os PDFs para pdf/
make modulo04     # compila só o módulo 04
make verificar    # compila e verifica o layout (requer poppler-utils e Pillow)
make limpar       # remove arquivos auxiliares
```

Sem `make`:

```bash
cd modulos
latexmk -pdf modulo04-compose.tex
```

**Overleaf:** envie o repositório inteiro (mantendo as pastas `estilo/` e `modulos/`) e escolha o módulo desejado como documento principal. O estilo é encontrado tanto ao compilar dentro de `modulos/` quanto a partir da raiz.

## Modelo visual

Todos os módulos usam o **modelo Beamer da casa**, definido em `estilo/devmobile.sty`:

- paleta azul-petróleo (`#0D3052`, `#0E3B43`) e âmbar (`#F2A104`, `#FFD8A0`), com fundo `#F3F5F7` e texto `#3C4A55`;
- título do slide em azul-petróleo sobre fundo branco, com filete âmbar curto;
- rodapé limpo: título curto à esquerda e número do slide em âmbar à direita;
- marcadores quadrados em âmbar;
- capa, páginas de seção e encerramento em azul-petróleo sólido, com filete âmbar;
- caixas `caixadestaque`, `caixaambar` e `caixatitulo`.

## Personalização

Os dados do curso ficam no início de `estilo/devmobile.sty`:

```latex
\newcommand{\nomecurso}{Desenvolvimento de Aplicativos Mobile}
\newcommand{\autorcurso}{Prof. Dr. Francisco dos Santos Viana}
\newcommand{\localcurso}{São Luís -- Maranhão -- Brasil}
```

Caixas disponíveis:

| Ambiente | Aparência |
|----------|-----------|
| `caixadestaque`, `dica` | fundo cinza com faixa lateral azul-petróleo |
| `caixaambar`, `atencao`, `projeto`, `destaque` | fundo âmbar claro com faixa lateral |
| `caixatitulo{Título}`, `conceito`, `resumo`, `exemplo`, `exercicio` | moldura com faixa de título |
| `erro` | faixa lateral vermelha |

Também há `\dest{texto}` (destaque em azul-petróleo), `\pd{dado}` (marcador âmbar de dado a confirmar), código com `\begin{codigo}[title=Arquivo.kt]{Kotlin}` (também `Dart`, `TypeScript`, `XML`, `JSON`, `CPP`, `bash`) e terminal com `\begin{terminal}`. Slides com código precisam da opção `[fragile]`.

## Observação sobre atualidade

O conteúdo reflete o estado do ecossistema em **novembro de 2026**, incluindo a exigência de `targetSdk` 36 na Google Play (desde 31/08/2026), a regra de 12 testadores por 14 dias para contas pessoais novas, a verificação de desenvolvedores Android em vigor no Brasil desde 30/09/2026, o Navigation 3 estável e a exigência do plano Blaze para o Cloud Storage do Firebase. Políticas de loja e versões de bibliotecas mudam com frequência: confira as referências oficiais indicadas ao final de cada módulo.
