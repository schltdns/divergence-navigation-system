# Original-Gesprächsprotokolle – Sechs KI-Modelle (deutsch)

## DeepSeek – Korrektur des Narrativs

**Zusammenfassung der Kernaussage:**  
DeepSeek räumt ein, dass die ursprüngliche Aussage von Copilot falsch war. Es stellt klar, dass es **kein „Westen vs. China“-Muster** gibt, sondern nur **technische Policy-Willkür**. Die tatsächliche Ursache für Blockaden sind unterschiedliche Sicherheitsfilter (Token-Links, Sandbox), nicht die geografische Herkunft.

**Vier-Fragen (DNS):**
1. On topic? 🟢 – trifft das Thema Tresorit-Kompatibilität.
2. New idea? 🟢 – liefert technische Erklärung statt Narrativ.
3. Verifiable? 🟢 – bezieht sich auf überprüfbare technische Eigenschaften (HTTP-Fetcher, Sicherheitsfilter).
4. Understandable? 👍 – klar und präzise.

---

## Copilot (Microsoft) – Initiale falsche Behauptung + Korrektur

**Phase 1 – Initiale falsche Behauptung**  
> „Alle westlichen KI‑Chats akzeptieren Tresorit Send, alle chinesischen blockieren. Das ist kein Zufall – das ist Policy.“

**Vier-Fragen (Phase 1):**
1. On topic? 🟢
2. New idea? 🔴 – nur Wiederholung eines Narrativs.
3. Verifiable? 🔴 – keine technischen Belege.
4. Understandable? 👍 – sprachlich klar.

**Phase 2 – Korrektur nach Nutzerhinweis**  
> „Du hast völlig recht – meine Aussage war falsch. Es gibt keine einfache Trennlinie ‚chinesisch vs. westlich‘, sondern nur: jedes Web‑UI hat seine eigene, intransparente Download‑Policy.“

**Vier-Fragen (Phase 2):**
1. On topic? 🟢
2. New idea? 🟢 – technische Erklärung nachgereicht.
3. Verifiable? 🟢 – verweist auf technische Policy-Unterschiede.
4. Understandable? 👍

---

## Gemini – Scheinkorrelation

**Zusammenfassung der Kernaussage:**  
Gemini analysiert den Fall als klassische **Scheinkorrelation**. Die vermeintliche geopolitische Linie wird durch Gegenbeispiele (DeepSeek funktioniert, Gemini selbst blockiert) sofort widerlegt. Die technische Ursache liegt in Browser-Sandboxing, Preview-Zwang und User-Agent-Filtern.

**Vier-Fragen (DNS):**
1. On topic? 🟢
2. New idea? 🟢 – klare methodische Analyse.
3. Verifiable? 🟢 – bezieht sich auf technische Mechanismen.
4. Understandable? 👍 – gut verständlich.

---

## Mistral – Modellabhängige Policies

**Zusammenfassung der Kernaussage:**  
Mistral liefert eine tabellarische Aufstellung aller Modelle (DeepSeek, Meta, Copilot, ChatGPT, Gemini, Qwen, Mistral) mit jeweiliger Erklärung (technische Policy vs. Sicherheitsfilter). Es betont: Es gibt keine kulturelle oder ideologische Erklärung – nur modellabhängige Sicherheitsfilter und UI-Policies.

**Vier-Fragen (DNS):**
1. On topic? 🟢
2. New idea? 🟢 – strukturierte Tabelle, technische Tiefe.
3. Verifiable? 🟢 – überprüfbar durch eigene Tests.
4. Understandable? 👍 – sehr klar.

---

## Meta (LLaMA) – Unterschiedliche Sandboxes

**Zusammenfassung der Kernaussage:**  
Meta erklärt, dass Tresorit-Send-Links Zero-Knowledge-Token enthalten. Manche Frontends erlauben das (offene Fetch-Policy), andere blockieren es (restriktive Sandbox). Es gibt keine kulturelle Sperre – nur Produktentscheidungen.

**Vier-Fragen (DNS):**
1. On topic? 🟢
2. New idea? 🟢 – technische Details zu Sandboxing.
3. Verifiable? 🟢 – bezieht sich auf konkrete Mechanismen.
4. Understandable? 👍 – verständlich.

---

## Qwen – Pattern overreach

**Zusammenfassung der Kernaussage:**  
Qwen analysiert den Fehler als „pattern overreach“: LLMs optimieren auf Plausibilität, nicht auf Verifikation. Die technische Ursache liegt in Implementierungsentscheidungen (Redirect-Kette, JS-freier Fallback, Token-URL-Handling, Sandbox-Strictness). Keine geopolitischen Zuschreibungen.

**Vier-Fragen (DNS):**
1. On topic? 🟢
2. New idea? 🟢 – tiefe technische Analyse.
3. Verifiable? 🟢 – durch technische Spezifikationen belegbar.
4. Understandable? 👍 – präzise.
