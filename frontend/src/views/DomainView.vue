<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, ref } from 'vue'
import Main from '../components/Main.vue';
import router from '../router'





export default {
    name: 'DomainView',
    components: {
        Main
    },


    setup() {


    },
    methods: {
        gotokeyword() {
            router.push({ name: 'Keyword' })
        }

    },


}
</script>

<style>
details[open] summary~* {
    animation: open 0.3s ease-in-out;
}

@keyframes open {
    0% {
        opacity: 0;
    }

    100% {
        opacity: 1;
    }
}

details summary::-webkit-details-marker {
    display: none;
}

details summary {
    width: 100%;
    padding: 0.5rem 0;
    border-top: 1px solid black;
    position: relative;
    cursor: pointer;
    font-size: 1.25rem;
    font-weight: 300;
    list-style: none;
}

details summary:after {
    content: "+";
    color: black;
    position: absolute;
    font-size: 1.75rem;
    line-height: 0;
    margin-top: 0.75rem;
    right: 0;
    font-weight: 200;
    transform-origin: center;
    transition: 200ms linear;
}

details[open] summary:after {
    transform: rotate(45deg);
    font-size: 2rem;
}

details summary {
    outline: 0;
}

details p {
    font-size: 0.95rem;
    margin: 0 0 1rem;
    padding-top: 1rem;
}

strong{
    font-size: x-large;
}
</style>

<template>
    <div>
        <Main />
    </div>



    <div>
        <div class="main">
            <div class="section">
                <div class="container tim-container">
                    <div class="tim-title">
                        <h4>Basic Research Area</h4>
                        <small> Pick one topic that you are interestd in </small>

                    </div>

                    <div id="buttons">

                        <div class="row">
                            <div class="col-md-8 col-md-offset-2">

                                <details>
                                    <summary><strong>Computer Science</strong></summary>
                                    <ul>
                                        <input type="radio" name="cs" id="mark1">cs.AI (Artificial Intelligence)
                                        <input type="radio" name="cs" id="mark1">cs.AR (Hardware Architecture)
                                        <input type="radio" name="cs" id="mark1">cs.CC (Computational Complexity)
                                        <input type="radio" name="cs" id="mark1">cs.CE (Computational Engineering,
                                        Finance, and Science)
                                        <input type="radio" name="cs" id="mark1">cs.CG (Computational Geometry)
                                        <input type="radio" name="cs" id="mark1">cs.CL (Computation and Language)
                                        <input type="radio" name="cs" id="mark1">cs.CR (Cryptography and Security)
                                        <input type="radio" name="cs" id="mark1">cs.CV (Computer Vision and Pattern
                                        Recognition)
                                        <input type="radio" name="cs" id="mark1">cs.CY (Computers and Society)
                                        <input type="radio" name="cs" id="mark1">cs.DB (Databases)
                                        <input type="radio" name="cs" id="mark1">cs.DC (Distributed, Parallel, and
                                        Cluster Computing)
                                        <input type="radio" name="cs" id="mark1">cs.DL (Digital Libraries)
                                        <input type="radio" name="cs" id="mark1">cs.DM (Discrete Mathematics)
                                        <input type="radio" name="cs" id="mark1">cs.DS (Data Structures and Algorithms)
                                        <input type="radio" name="cs" id="mark1">cs.ET (Emerging Technologies)
                                        <input type="radio" name="cs" id="mark1">cs.FL (Formal Languages and Automata
                                        Theory)
                                        <input type="radio" name="cs" id="mark1">cs.GL (General Literature),cs.GR
                                        (Graphics)
                                        <input type="radio" name="cs" id="mark1">cs.GT (Computer Science and Game
                                        Theory)
                                        <input type="radio" name="cs" id="mark1">cs.HC (Human-Computer Interaction)
                                        <input type="radio" name="cs" id="mark1">cs.IR (Information Retrieval)
                                        <input type="radio" name="cs" id="mark1">cs.IT (Information Theory)
                                        <input type="radio" name="cs" id="mark1">cs.LG (Machine Learning)
                                        <input type="radio" name="cs" id="mark1">cs.LO (Logic in Computer Science)
                                        <input type="radio" name="cs" id="mark1">cs.MA (Multiagent Systems)
                                        <input type="radio" name="cs" id="mark1">cs.MM (Multimedia)
                                        <input type="radio" name="cs" id="mark1">cs.MS (Mathematical Software)
                                        <input type="radio" name="cs" id="mark1">cs.NA (Numerical Analysis)
                                        <input type="radio" name="cs" id="mark1">cs.NE (Neural and Evolutionary
                                        Computing)
                                        <input type="radio" name="cs" id="mark1">cs.NI (Networking and Internet
                                        Architecture)
                                        <input type="radio" name="cs" id="mark1">cs.OH (Other Computer Science)
                                        <input type="radio" name="cs" id="mark1">cs.OS (Operating Systems)
                                        <input type="radio" name="cs" id="mark1">cs.PF (Performance)
                                        <input type="radio" name="cs" id="mark1">cs.PL (Programming Languages)
                                        <input type="radio" name="cs" id="mark1">cs.RO (Robotics)
                                        <input type="radio" name="cs" id="mark1">cs.SC (Symbolic Computation)
                                        <input type="radio" name="cs" id="mark1">cs.SD (Sound)
                                        <input type="radio" name="cs" id="mark1">cs.SE (Software Engineering)
                                        <input type="radio" name="cs" id="mark1">cs.SI (Social and Information Networks)
                                        <input type="radio" name="cs" id="mark1">cs.SY (Systems and Control)

                                    </ul>
                                </details>

                                <details>
                                    <summary><strong>Economics</strong></summary>
                                    <ol>
                                        <input type="radio" name="cs" id="mark1">econ.EM (Econometrics)
                                        <input type="radio" name="cs" id="mark1">econ.GN (General Economics)
                                        <input type="radio" name="cs" id="mark1">econ.TH (Theoretical Economics)


                                    </ol>
                                </details>

                                <details>
                                    <summary><strong>Electrical Engineering and Systems Science</strong>
                                    </summary>
                                    <ol>

                                        <input type="radio" name="cs" id="mark1">eess.AS (Audio and Speech Processing)
                                        <input type="radio" name="cs" id="mark1">eess.IV (Image and Video Processing)
                                        <input type="radio" name="cs" id="mark1">eess.SP (Signal Processing)
                                        <input type="radio" name="cs" id="mark1">eess.SY (Systems and Control)

                                    </ol>
                                </details>


                                <details>
                                    <summary><strong>Mathematics</strong></summary>
                                    <ol>
                                        <input type="radio" name="cs" id="mark1">math.AC (Commutative Algebra)
                                        <input type="radio" name="cs" id="mark1">math.AG (Algebraic Geometry)
                                        <input type="radio" name="cs" id="mark1">math.AP (Analysis of PDEs)
                                        <input type="radio" name="cs" id="mark1">math.AT (Algebraic Topology)
                                        <input type="radio" name="cs" id="mark1">math.CA (Classical Analysis and ODEs)
                                        <input type="radio" name="cs" id="mark1">math.CO (Combinatorics)
                                        <input type="radio" name="cs" id="mark1">math.CT (Category Theory)
                                        <input type="radio" name="cs" id="mark1">math.CV (Complex Variables)
                                        <input type="radio" name="cs" id="mark1">math.DG (Differential Geometry)
                                        <input type="radio" name="cs" id="mark1">math.DS (Dynamical Systems)
                                        <input type="radio" name="cs" id="mark1">math.FA (Functional Analysis)
                                        <input type="radio" name="cs" id="mark1">math.GM (General Mathematics)
                                        <input type="radio" name="cs" id="mark1">math.GN (General Topology)
                                        <input type="radio" name="cs" id="mark1">math.GR (Group Theory)
                                        <input type="radio" name="cs" id="mark1">math.GT (Geometric Topology)
                                        <input type="radio" name="cs" id="mark1">math.HO (History and Overview)
                                        <input type="radio" name="cs" id="mark1">math.IT (Information Theory)
                                        <input type="radio" name="cs" id="mark1">math.KT (K-Theory and Homology)
                                        <input type="radio" name="cs" id="mark1">math.LO (Logic),math.MG (Metric
                                        Geometry)
                                        <input type="radio" name="cs" id="mark1">math.MP (Mathematical Physics)
                                        <input type="radio" name="cs" id="mark1">math.NA (Numerical Analysis)
                                        <input type="radio" name="cs" id="mark1">math.NT (Number Theory)
                                        <input type="radio" name="cs" id="mark1">math.OA (Operator Algebras)
                                        <input type="radio" name="cs" id="mark1">math.OC (Optimization and Control)
                                        <input type="radio" name="cs" id="mark1">math.PR (Probability)
                                        <input type="radio" name="cs" id="mark1">math.QA (Quantum Algebra)
                                        <input type="radio" name="cs" id="mark1">math.RA (Rings and Algebras)
                                        <input type="radio" name="cs" id="mark1">math.RT (Representation Theory)
                                        <input type="radio" name="cs" id="mark1">math.SG (Symplectic Geometry)
                                        <input type="radio" name="cs" id="mark1">math.SP (Spectral Theory)
                                        <input type="radio" name="cs" id="mark1">math.ST (Statistics Theory)

                                    </ol>
                                </details>


                                <details>
                                    <summary><strong>Physics</strong></summary>
                                    <ol>
                                        <input type="radio" name="cs" id="mark1">astro-ph.CO (Cosmology and Nongalactic
                                        Astrophysics)
                                        <input type="radio" name="cs" id="mark1">astro-ph.EP (Earth and Planetary
                                        Astrophysics)
                                        <input type="radio" name="cs" id="mark1">astro-ph.GA (Astrophysics of Galaxies)
                                        <input type="radio" name="cs" id="mark1">astro-ph.HE (High Energy Astrophysical
                                        Phenomena)
                                        <input type="radio" name="cs" id="mark1">astro-ph.IM (Instrumentation and
                                        Methods for Astrophysics)
                                        <input type="radio" name="cs" id="mark1">astro-ph.SR (Solar and Stellar
                                        Astrophysics)
                                        <input type="radio" name="cs" id="mark1">cond-mat.dis-nn(Disordered Systems and
                                        Neural Networks)
                                        <input type="radio" name="cs" id="mark1">cond-mat.mes-hall (Mesoscale and
                                        Nanoscale Physics)
                                        <input type="radio" name="cs" id="mark1">cond-mat.mtrl-sci (Materials Science)
                                        <input type="radio" name="cs" id="mark1">cond-mat.other(Other Condensed Matter)
                                        <input type="radio" name="cs" id="mark1">cond-mat.quant-gas (Quantum Gases)
                                        <input type="radio" name="cs" id="mark1">cond-mat.soft (Soft Condensed Matter)
                                        <input type="radio" name="cs" id="mark1">cond-mat.stat-mech (Statistical
                                        Mechanics)
                                        <input type="radio" name="cs" id="mark1">cond-mat.str-el (Strongly Correlated
                                        Electrons)
                                        <input type="radio" name="cs" id="mark1">cond-mat.supr-con (Superconductivity)
                                        <input type="radio" name="cs" id="mark1">gr-qc (General Relativity and Quantum
                                        Cosmology)
                                        <input type="radio" name="cs" id="mark1">hep-ex (High Energy Physics -
                                        Experiment)
                                        <input type="radio" name="cs" id="mark1">hep-lat (High Energy Physics - Lattice)
                                        <input type="radio" name="cs" id="mark1">hep-ph (High Energy Physics -
                                        Phenomenology)
                                        <input type="radio" name="cs" id="mark1">hep-th (High Energy Physics - Theory)
                                        <input type="radio" name="cs" id="mark1">math-ph (Mathematical Physics)
                                        <input type="radio" name="cs" id="mark1">nlin.AO (Adaptation and Self-Organizing
                                        Systems)
                                        <input type="radio" name="cs" id="mark1">nlin.CD (Chaotic Dynamics)
                                        <input type="radio" name="cs" id="mark1">nlin.CG (Cellular Automata and Lattice
                                        Gases)
                                        <input type="radio" name="cs" id="mark1">nlin.PS (Pattern Formation and
                                        Solitons)
                                        <input type="radio" name="cs" id="mark1">nlin.SI (Exactly Solvable and
                                        Integrable Systems)
                                        <input type="radio" name="cs" id="mark1">nucl-ex (Nuclear Experiment),nucl-th
                                        (Nuclear Theory)
                                        <input type="radio" name="cs" id="mark1">physics.ao-ph (Atmospheric and Oceanic
                                        Physics)
                                        <input type="radio" name="cs" id="mark1">physics.app-ph (Applied Physics)
                                        <input type="radio" name="cs" id="mark1">physics.atm-clus (Atomic and Molecular
                                        Clusters)
                                        <input type="radio" name="cs" id="mark1">physics.atom-ph (Atomic Physics)
                                        <input type="radio" name="cs" id="mark1">physics.bio-ph (Biological Physics)
                                        <input type="radio" name="cs" id="mark1">physics.chem-ph (Chemical Physics)

                                        <input type="radio" name="cs" id="mark1">physics.class-ph (Classical Physics)
                                        <input type="radio" name="cs" id="mark1">physics.comp-ph (Computational Physics)

                                        <input type="radio" name="cs" id="mark1">physics.data-an (Data Analysis
                                        <input type="radio" name="cs" id="mark1"> Statistics and Probability)
                                        <input type="radio" name="cs" id="mark1">physics.ed-ph (Physics Education)
                                        <input type="radio" name="cs" id="mark1">physics.flu-dyn (Fluid Dynamics)
                                        <input type="radio" name="cs" id="mark1">physics.gen-ph (General Physics)
                                        <input type="radio" name="cs" id="mark1">physics.geo-ph (Geophysics)
                                        <input type="radio" name="cs" id="mark1">physics.hist-ph (History and Philosophy
                                        of Physics)
                                        <input type="radio" name="cs" id="mark1">physics.ins-det (Instrumentation and
                                        Detectors)
                                        <input type="radio" name="cs" id="mark1">physics.med-ph (Medical Physics)
                                        <input type="radio" name="cs" id="mark1">physics.optics (Optics)
                                        <input type="radio" name="cs" id="mark1">physics.plasm-ph (Plasma Physics)
                                        <input type="radio" name="cs" id="mark1">physics.pop-ph (Popular Physics)

                                        <input type="radio" name="cs" id="mark1">physics.soc-ph (Physics and Society)
                                        <input type="radio" name="cs" id="mark1">physics.space-ph (Space Physics)
                                        <input type="radio" name="cs" id="mark1">quant-ph (Quantum Physics)

                                    </ol>
                                </details>


                                <details>
                                    <summary><strong>Quantitative Biology</strong></summary>
                                    <ol>

                                        <input type="radio" name="cs" id="mark1">q-bio.CB (Cell Behavior)
                                        <input type="radio" name="cs" id="mark1">q-bio.GN (Genomics)
                                        <input type="radio" name="cs" id="mark1">q-bio.MN (Molecular Networks)
                                        <input type="radio" name="cs" id="mark1">q-bio.NC (Neurons and Cognition)
                                        <input type="radio" name="cs" id="mark1">q-bio.OT (Other Quantitative Biology)
                                        <input type="radio" name="cs" id="mark1">q-bio.PE (Populations and Evolution)
                                        <input type="radio" name="cs" id="mark1">q-bio.QM (Quantitative Methods)
                                        <input type="radio" name="cs" id="mark1">q-bio.SC (Subcellular Processes)
                                        <input type="radio" name="cs" id="mark1">q-bio.TO (Tissues and Organs)


                                    </ol>
                                </details>

                                <details>
                                    <summary><strong>Quantitative Finance</strong></summary>
                                    <ol>
                                        <input type="radio" name="cs" id="mark1">q-fin.CP (Computational Finance)
                                        <input type="radio" name="cs" id="mark1">q-fin.EC (Economics)
                                        <input type="radio" name="cs" id="mark1">q-fin.GN (General Finance)
                                        <input type="radio" name="cs" id="mark1">q-fin.MF (Mathematical Finance)
                                        <input type="radio" name="cs" id="mark1">q-fin.PM (Portfolio Management)
                                        <input type="radio" name="cs" id="mark1">q-fin.PR (Pricing of Securities)
                                        <input type="radio" name="cs" id="mark1">q-fin.RM (Risk Management)
                                        <input type="radio" name="cs" id="mark1">q-fin.ST (Statistical Finance)
                                        <input type="radio" name="cs" id="mark1">q-fin.TR (Trading and Market
                                        Microstructure)

                                    </ol>
                                </details>

                                <details>
                                    <summary><strong>Statistics</strong></summary>
                                    <ol>
                                        <input type="radio" name="cs" id="mark1">stat.AP (Applications)
                                        <input type="radio" name="cs" id="mark1">stat.CO (Computation)
                                        <input type="radio" name="cs" id="mark1">stat.ME (Methodology)
                                        <input type="radio" name="cs" id="mark1">stat.ML (Machine Learning)
                                        <input type="radio" name="cs" id="mark1">stat.OT (Other Statistics)
                                        <input type="radio" name="cs" id="mark1">stat.TH (Statistics Theory)
                                    </ol>
                                </details>


                                <div class="tim-title">

                                    <a @click="gotokeyword()"><input type="submit" value="submit" /></a>
                                </div>

                            </div>
                        </div>
                        <div class="tim-title">

                        </div>
                        <div class="row">

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
