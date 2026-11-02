# DevMobile: Desenvolvimento de Aplicativos Mobile

Curso completo de desenvolvimento mobile em **slides Beamer (LaTeX)**, no modelo da casa (azul-petróleo e âmbar), do iniciante ao avançado. São **21 módulos** (00 a 20) organizados em **duas trilhas** que compartilham a mesma numeração:

- **Trilha Kotlin**: Android nativo com Kotlin, Jetpack Compose, coroutines, Room, Retrofit, Hilt e Firebase.
- **Trilha Flutter**: Android e iOS (e também web e desktop) com Dart, Flutter, Riverpod/Bloc, Drift, Dio e FlutterFire.

Sete módulos são **comuns** às duas trilhas: ecossistema mobile, engenharia de software e Git, design e UX, banco de dados, *backend* terceirizado (BaaS), *backend* próprio e engenharia avançada. Um projeto integrador, o **LabMonitor** (app para laboratórios de eletroeletrônica, com sensores ESP32 via BLE e MQTT), evolui ao longo de todos os módulos.

> Os PDFs compilados ficam em [`pdf/comum`](pdf/comum), [`pdf/kotlin`](pdf/kotlin) e [`pdf/flutter`](pdf/flutter): no total, 35 apresentações e cerca de 1 360 slides.

## Como cada módulo é organizado

Todos os módulos seguem a mesma estrutura didática:

1. **Objetivos** e **roteiro** do módulo.
2. **Fundamentos** (teoria e conceitos): definições, como as coisas funcionam por dentro, analogias, um pouco de história e diagramas. A teoria comum às duas trilhas fica em [`modulos/fundamentos/`](modulos/fundamentos) e é incluída pelos dois decks do mesmo número.
3. **Prática** na trilha escolhida, com código comentado do LabMonitor.
4. **Fechamento**: resumo, glossário, questões de revisão, exercícios, a etapa do projeto LabMonitor, referências oficiais e as **respostas comentadas** das questões.

As caixas têm papéis fixos, explicados no Módulo 00 (``Como ler estes slides''):

| Caixa | Uso |
|-------|-----|
| `definicao` | definição formal de um conceito |
| `conceito` | ideia-chave ou princípio |
| `pordentro` | como funciona por dentro |
| `analogia` | comparação com algo do dia a dia |
| `historia` | origem e evolução |
| `exemplo` | caso concreto, em geral do LabMonitor |
| `dica` / `atencao` / `erro` | boa prática / cuidado / erro comum |
| `exercicio` / `projeto` | atividade / etapa do LabMonitor |

## Grade do curso

| Nº | Nível | Trilha Kotlin | Trilha Flutter |
|----|-------|---------------|----------------|
| 00 | Iniciante | [Apresentação e ecossistema mobile](modulos/comum/modulo00-apresentacao.tex) *(comum)* | *(comum)* |
| 01 | Iniciante | [Ambiente: Android Studio, Gradle, ADB](modulos/kotlin/modulo01-ambiente.tex) | [Ambiente: Flutter SDK, DevTools](modulos/flutter/modulo01-ambiente.tex) |
| 02 | Iniciante | [Kotlin essencial](modulos/kotlin/modulo02-kotlin.tex) | [Dart essencial](modulos/flutter/modulo02-dart.tex) |
| 03 | Iniciante | [Engenharia de software e Git](modulos/comum/modulo03-engenharia-git.tex) *(comum)* | *(comum)* |
| 04 | Iniciante | [Design de interfaces e UX](modulos/comum/modulo04-design-ux.tex) *(comum)* | *(comum)* |
| 05 | Iniciante | [Interfaces com Jetpack Compose](modulos/kotlin/modulo05-compose.tex) | [Widgets e layouts](modulos/flutter/modulo05-widgets.tex) |
| 06 | Iniciante | [Coroutines e Flow](modulos/kotlin/modulo06-coroutines.tex) | [Dart assíncrono: Future, Stream, Isolates](modulos/flutter/modulo06-assincrono.tex) |
| 07 | Iniciante | [Estado, navegação e animações](modulos/kotlin/modulo07-estado-navegacao.tex) | [Estado, navegação e animações](modulos/flutter/modulo07-estado-navegacao.tex) |
| 08 | Intermediário | [Arquitetura: MVVM, camadas, Hilt](modulos/kotlin/modulo08-arquitetura.tex) | [Arquitetura e gerência de estado](modulos/flutter/modulo08-arquitetura.tex) |
| 09 | Intermediário | [Fundamentos de banco de dados](modulos/comum/modulo09-banco-de-dados.tex) *(comum)* | *(comum)* |
| 10 | Intermediário | [Persistência: DataStore e Room](modulos/kotlin/modulo10-persistencia.tex) | [Persistência: sqflite e Drift](modulos/flutter/modulo10-persistencia.tex) |
| 11 | Intermediário | [Rede e APIs: Retrofit e OkHttp](modulos/kotlin/modulo11-rede-apis.tex) | [Rede e APIs: http e Dio](modulos/flutter/modulo11-rede-apis.tex) |
| 12 | Intermediário | [Firebase](modulos/kotlin/modulo12-firebase.tex) | [Firebase com FlutterFire](modulos/flutter/modulo12-firebase.tex) |
| 13 | Intermediário | [Dispositivo e IoT: sensores, BLE, MQTT](modulos/kotlin/modulo13-dispositivo-iot.tex) | [Dispositivo e IoT: câmera, GPS, BLE, NFC, serial, MQTT](modulos/flutter/modulo13-dispositivo.tex) |
| 14 | Intermediário | [Testes e qualidade](modulos/kotlin/modulo14-testes-qualidade.tex) | [Testes e qualidade](modulos/flutter/modulo14-testes.tex) |
| 15 | Intermediário | [Publicação na Google Play](modulos/kotlin/modulo15-publicacao.tex) | [Publicação: Google Play e App Store](modulos/flutter/modulo15-publicacao.tex) |
| 16 | Avançado | [*Backend* terceirizado (BaaS)](modulos/comum/modulo16-backend-baas.tex) *(comum)* | *(comum)* |
| 17 | Avançado | [*Backend* próprio: REST, PostgreSQL, JWT, Docker](modulos/comum/modulo17-backend-proprio.tex) *(comum)* | *(comum)* |
| 18 | Avançado | [Engenharia avançada: modularização, desempenho, observabilidade, CI/CD](modulos/comum/modulo18-engenharia-avancada.tex) *(comum)* | *(comum)* |
| 19 | Avançado | [Multiplataforma: Flutter, React Native, KMP](modulos/kotlin/modulo19-multiplataforma.tex) | [Código nativo, web, desktop e embarcados](modulos/flutter/modulo19-nativo-multiplataforma.tex) |
| 20 | Avançado | [IA, segurança, monetização e projeto final](modulos/kotlin/modulo20-avancados-projeto.tex) | [IA, segurança, monetização e projeto final](modulos/flutter/modulo20-avancados-projeto.tex) |

### Teoria compartilhada (`modulos/fundamentos/`)

| Arquivo | Assuntos |
|---------|----------|
| `f01-ambiente` | compilação e execução, SDK e IDE, sistemas de build, emuladores, depuração |
| `f02-linguagens` | paradigmas, sistemas de tipos, *null safety*, orientação a objetos, funcional, memória |
| `f05-ui-declarativa` | imperativo × declarativo, composição, layout por restrições, pipeline de um quadro, recomposição, chaves, temas, densidade |
| `f06-concorrencia` | processos e *threads*, concorrência × paralelismo, I/O × CPU, laço de eventos, *async/await*, concorrência estruturada, condições de corrida, fluxos |
| `f07-estado-navegacao` | estado e fonte única da verdade, fluxo unidirecional, máquinas de estados, ciclo de vida, morte do processo, navegação e *deep links*, animação |
| `f08-arquitetura` | arquitetura de software, MVC a MVI, arquitetura limpa e hexagonal, inversão e injeção de dependência, ADRs |
| `f10-persistencia` | hierarquia de memória, *sandbox* de arquivos, mapeamento objeto-relacional, migrações, cache, *offline-first*, conflitos, criptografia em repouso |
| `f11-redes` | TCP/IP, NAT e DNS, TCP × UDP, TLS, HTTP/1.1 a HTTP/3, cache HTTP, serialização, redes móveis, tempo real |
| `f12-identidade-nuvem` | OAuth 2.0 e OpenID Connect, *tokens*, *passkeys*, bancos em tempo real, regras de segurança, *push*, funções por eventos |
| `f13-dispositivo` | ADC e amostragem, sensores MEMS, filtragem e fusão, GNSS, permissões, BLE, MQTT, UART, NFC, energia |
| `f14-testes` | erro × defeito × falha, níveis e técnicas de teste, cobertura, dublês, TDD/BDD, ISO 25010 |
| `f15-publicacao` | assinatura digital, versionamento, pacotes, lojas, LGPD, gestão de lançamentos, ASO, saúde do app |
| `f19-multiplataforma` | espectro das abordagens, execução e renderização, pontes e FFI, PWA, matriz de decisão |
| `f20-avancados` | IA e LLMs, segurança da informação (STRIDE, OWASP), produto e métricas de negócio |

## Estrutura do repositório

```
DevMobile/
├── estilo/
│   └── devmobile.sty            # modelo da casa: cores, capa, seções, caixas, código, TikZ
├── modulos/
│   ├── comum/                   # módulos 00, 03, 04, 09, 16, 17 e 18
│   ├── kotlin/                  # trilha Kotlin
│   ├── flutter/                 # trilha Flutter
│   └── fundamentos/             # teoria compartilhada, incluída pelos dois decks
├── pdf/
│   ├── comum/  kotlin/  flutter/  # PDFs compilados
├── ferramentas/
│   └── verificar_layout.py      # checa erros, overfull boxes e slides transbordando
├── Makefile
└── .github/workflows/slides.yml # compila e verifica tudo a cada push
```

## Como compilar

Requisitos: TeX Live com `beamer`, `tcolorbox`, `listings`, `pgf/tikz` e `babel-portuguese` (no Debian/Ubuntu: `texlive-latex-extra`, `texlive-pictures`, `texlive-fonts-recommended` e `texlive-lang-portuguese`).

```bash
make              # compila os 35 decks e copia os PDFs para pdf/
make kotlin       # só a trilha Kotlin (use também: comum, flutter)
make modulo05     # o módulo 05 das duas trilhas
make verificar    # compila e verifica o layout (requer poppler-utils e Pillow)
make limpar       # remove arquivos auxiliares
```

Sem `make`, compile de dentro da pasta do módulo:

```bash
cd modulos/flutter
latexmk -pdf modulo05-widgets.tex
```

**Overleaf:** envie o repositório inteiro, mantendo as pastas `estilo/` e `modulos/`, e escolha o módulo desejado como documento principal. O estilo e os fundamentos são encontrados por caminhos relativos.

## Modelo visual e personalização

Todos os decks usam o **modelo Beamer da casa**, definido em `estilo/devmobile.sty`: paleta azul-petróleo (`#0D3052`, `#0E3B43`) e âmbar (`#F2A104`, `#FFD8A0`), fundo `#F3F5F7`, texto `#3C4A55`; capa, seções e encerramento em azul-petróleo sólido com filete âmbar; rodapé com trilha, módulo e número do slide. A capa mostra a trilha e o nível (00--07 iniciante, 08--15 intermediário, 16--20 avançado).

Os dados do curso ficam no início do estilo:

```latex
\newcommand{\nomecurso}{Desenvolvimento Mobile}
\newcommand{\autorcurso}{Prof. Dr. Francisco dos Santos Viana}
\newcommand{\localcurso}{São Luís -- Maranhão -- Brasil}
```

Cada deck começa com `\modulo[Kotlin]{05}{Título}{Subtítulo}` (ou `[Flutter]`; sem a opção, o módulo é comum). Código vai em `\begin{codigo}[title=Arquivo.kt]{Kotlin}` (também `Dart`, `Swift`, `TypeScript`, `XML`, `JSON`, `YAML`, `SQL`, `CPP`, `C` e `bash`) e terminal em `\begin{terminal}`; slides com código precisam da opção `[fragile]`. O fechamento usa os ambientes `glossario`, `questoes` e `respostas`.

## Observação sobre atualidade

O conteúdo reflete o ecossistema em **novembro de 2026**: `targetSdk` 36 exigido pela Google Play desde 31/08/2026 (com as mudanças do Android 16 para telas grandes e voltar preditivo), regra de 12 testadores por 14 dias para contas pessoais novas, verificação de desenvolvedores Android em vigor no Brasil desde 30/09/2026, Xcode 26 e SDK do iOS 26 exigidos pela App Store Connect desde 28/04/2026, Navigation 3 estável, plano Blaze para o Cloud Storage do Firebase e Dart executado na *thread* principal no Flutter (desde a versão 3.29). Políticas de loja e versões de bibliotecas mudam com frequência: confira as referências oficiais indicadas ao final de cada módulo.
