\section{Related Work and Distinction}

The \textit{Divergence-based Navigation System (DNS)} – previously developed under the working title ``Triangulation nach Schult'' – operates at the intersection of Multi-Agent Systems (MAS) and Epistemic Uncertainty. To define its unique contribution, it must be distinguished from existing frameworks:

\begin{itemize}
    \item \textbf{SCOUT (Uncertainty Triangulation):} While SCOUT utilizes signals like model heterogeneity and reasoning-critique for automated error detection in clinical settings, it lacks the \textbf{Phase P6 (Meta-Reflection)} characteristic of the DNS protocol. SCOUT aims to ``fix'' the AI; DNS aims to ``inform'' the human operator through structured dissonance.
    
    \item \textbf{AI Council Framework:} Traditional ``Councils'' orchestrate multiple LLMs to reach a \textbf{consensus} through deliberation. In contrast, DNS treats \textit{divergence} as the primary informative signal. We argue that forcing consensus often masks underlying epistemic risks.
    
    \item \textbf{Semantic Triangulation:} This mathematical approach focuses on consistency across linguistic transformations of a single problem. DNS, however, leverages the \textbf{diverse ``identities'' and training biases} of independent models (e.g., Grok vs. Claude) to expose structural blind spots.
    
    \item \textbf{DelphiAgent / LLM Council-Double Delphi:} These methods adapt the classical Delphi technique for iterative convergence. While they share a multi-stage structure, DNS is explicitly designed for \textbf{Falsification (P1)} and the analysis of unresolved gaps, rather than seeking a common denominator.
\end{itemize}

In summary, DNS is not a consensus-machine but a \textbf{diagnostic framework for uncertainty}, placing the human operator in the role of a ``Synthesizer'' rather than a mere recipient of an averaged output.
