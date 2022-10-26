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
    data() {
        return {
            SelectTopic: '',
        }
    },

    setup() {


    },
    methods: {
        gotokeyword() {
            router.push({ name: 'Keyword' ,params:{"topic":this.SelectTopic}})
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

strong {
    font-size: x-large;
}
label{
    padding: 5px;
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
                        <div  style="display:flex;" > 
                            <button :disabled="SelectTopic=== ''" class="btn btn-fill btn-primary" @click="gotokeyword()" style="margin-left:auto ;">Next</button>
                         </div>
                 

                    
                        <div class="row">
                            <div class="col-md-8 col-md-offset-2">

                                <details>
                                    <summary><strong>Computer Science</strong></summary>
                                    <ul>
                                       <label><input type="radio"  id="cs.AI" value="cs.AI(Artificial Intelligence" v-model="SelectTopic"   >Artificial Intelligence</label>
                                       <label><input type="radio"  id="cs.AR" value="cs.AR(Hardware Architecture" v-model="SelectTopic"   >Hardware Architecture</label>
                                       <label><input type="radio"  id="cs.CC" value="cs.CC(Computational Complexity" v-model="SelectTopic"   >Computational Complexity</label>
                                       <label><input type="radio"  id="cs.CE" value="cs.CE(Computational Engineering,Finance, and Science" v-model="SelectTopic"   >Computational Engineering, Finance, and Science</label>
                                       <label><input type="radio"  id="cs.CG" value="cs.CG(Computational Geometry" v-model="SelectTopic"   >Computational Geometry</label>
                                       <label><input type="radio"  id="cs.CL" value="cs.CL(Computation and Language" v-model="SelectTopic"   >Computation and Language</label>
                                       <label><input type="radio"  id="cs.CR" value="cs.CR(Cryptography and Security" v-model="SelectTopic"   >Cryptography and Security</label>
                                       <label><input type="radio"  id="cs.CV" value="cs.CV(Computer Vision and Pattern Recognition" v-model="SelectTopic"   >Computer Vision and Pattern Recognition</label>
                                       <label><input type="radio"  id="cs.CY" value="cs.CY(Computers and Society" v-model="SelectTopic"   >Computers and Society</label>
                                       <label><input type="radio"  id="cs.DB" value="cs.DB(Databases" v-model="SelectTopic"   >Databases</label>
                                       <label><input type="radio"  id="cs.DC" value="cs.DC(Distributed, Parallel, and Cluster Computing" v-model="SelectTopic"   >Distributed, Parallel, and Cluster Computing</label>
                                       <label><input type="radio"  id="cs.DL" value="cs.DL(Digital Libraries" v-model="SelectTopic"   >Digital Libraries</label>
                                       <label><input type="radio"  id="cs.DM" value="cs.DM(Discrete Mathematics" v-model="SelectTopic"   >Discrete Mathematics</label>
                                       <label><input type="radio"  id="cs.DS" value="cs.DS(Data Structures and Algorithms" v-model="SelectTopic"   >Data Structures and Algorithms</label>
                                       <label><input type="radio"  id="cs.ET" value="cs.ET (Emerging Technologies" v-model="SelectTopic"   >Emerging Technologies</label>
                                       <label><input type="radio"  id="cs.FL" value="cs.FL(Formal Languages and Automata Theory" v-model="SelectTopic"   >Formal Languages and Automata Theory</label>
                                       <label><input type="radio"  id="cs.GL" value="cs.GL(General Literature" v-model="SelectTopic"   >General Literature</label>
                                       <label><input type="radio"  id="cs.GR" value="cs.GR(Graphics" v-model="SelectTopic"   >Graphics</label>
                                       <label><input type="radio"  id="cs.GT" value="cs.GT(Computer Science and Game Theory" v-model="SelectTopic"   >Computer Science and Game Theory</label>
                                       <label><input type="radio"  id="cs.HC" value="cs.HC(Human-Computer Interaction" v-model="SelectTopic"   >Human-Computer Interaction</label>
                                       <label><input type="radio"  id="cs.IR" value="cs.IR(Information Retrieval" v-model="SelectTopic"   >Information Retrieval</label>
                                       <label><input type="radio"  id="cs.IT" value="cs.IT(Information Theory" v-model="SelectTopic"   >Information Theory</label>
                                       <label><input type="radio"  id="cs.LG" value="cs.LG(Machine Learning" v-model="SelectTopic"   >Machine Learning</label>
                                       <label><input type="radio"  id="cs.LO" value="cs.LO(Logic in Computer Science" v-model="SelectTopic"   >Logic in Computer Science</label>
                                       <label><input type="radio"  id="cs.MA" value="cs.MA(Multiagent Systems" v-model="SelectTopic"   >Multiagent Systems</label>
                                       <label><input type="radio"  id="cs.MM" value="cs.MM(Multimedia" v-model="SelectTopic"   >Multimedia</label>
                                       <label><input type="radio"  id="cs.MS" value="cs.MS(Mathematical Software" v-model="SelectTopic"   >Mathematical Software</label>
                                       <label><input type="radio"  id="cs.NA" value="cs.NA(Numerical Analysis" v-model="SelectTopic"   >Numerical Analysis</label>
                                       <label><input type="radio"  id="cs.NE" value="cs.NE(Neural and Evolutionary Computing" v-model="SelectTopic"   >Neural and Evolutionary Computing</label>
                                       <label><input type="radio"  id="cs.NI" value="cs.NI(Networking and Internet Architecture" v-model="SelectTopic"   >Networking and Internet Architecture</label>
                                       <label><input type="radio"  id="cs.OH" value="cs.OH(Other Computer Science" v-model="SelectTopic"   >Other Computer Science</label>
                                       <label><input type="radio"  id="cs.OS" value="cs.OS(Operating Systems" v-model="SelectTopic"   >Operating Systems</label>
                                       <label><input type="radio"  id="cs.PF" value="cs.PF(Performance" v-model="SelectTopic"   >Performance</label>
                                       <label><input type="radio"  id="cs.PL" value="cs.PL(Programming Languages" v-model="SelectTopic"   >Programming Languages</label>
                                       <label><input type="radio"  id="cs.RO" value="cs.RO(Robotics" v-model="SelectTopic"   >Robotics</label>
                                       <label><input type="radio"  id="cs.SC" value="cs.SC(Symbolic Computation" v-model="SelectTopic"   >Symbolic Computation</label>
                                       <label><input type="radio"  id="cs.SD" value="cs.SD(Sound" v-model="SelectTopic"   >Sound</label>
                                       <label><input type="radio"  id="cs.SE" value="cs.SE(Software Engineering" v-model="SelectTopic"   >Software Engineering</label>
                                       <label><input type="radio"  id="cs.SI" value="cs.SI(Social and Information Networks" v-model="SelectTopic"   >Social and Information Networks</label>
                                       <label><input type="radio"  id="cs.SY" value="cs.SY(Systems and Control" v-model="SelectTopic"   >Systems and Control</label>

                                    </ul>
                                </details>

                                <details>
                                    <summary><strong>Economics</strong></summary>
                                    <ol>
                                       <label><input type="radio"  id="econ.EM" value="econ.EM(Econometrics" v-model="SelectTopic"   >Econometrics</label>
                                       <label><input type="radio"  id="econ.GN" value="econ.GN(General Economics" v-model="SelectTopic"   >General Economics</label>
                                       <label><input type="radio"  id="econ.TH" value="econ.TH(Theoretical Economics" v-model="SelectTopic"   >Theoretical Economics</label>


                                    </ol>
                                </details>

                                <details>
                                    <summary><strong>Electrical Engineering and Systems Science</strong>
                                    </summary>
                                    <ol>

                                       <label><input type="radio"  id="eess.AS" value="eess.AS(Audio and Speech Processing" v-model="SelectTopic"   >Audio and Speech Processing</label>
                                       <label><input type="radio"  id="eess.IV" value="eess.IV(Image and Video Processing" v-model="SelectTopic"   >Image and Video Processing</label>
                                       <label><input type="radio"  id="eess.SP" value="eess.SP(Signal Processing" v-model="SelectTopic"   >Signal Processing</label>
                                       <label><input type="radio"  id="eess.SY" value="eess.SY(Systems and Control" v-model="SelectTopic"   >Systems and Control</label>

                                    </ol>
                                </details>


                                <details>
                                    <summary><strong>Mathematics</strong></summary>
                                    <ol>
                                       <label><input type="radio"  id="math.AC" value="math.AC(Commutative Algebra" v-model="SelectTopic"   >Commutative Algebra</label>
                                       <label><input type="radio"  id="math.AG" value="math.AG(Algebraic Geometry" v-model="SelectTopic"   >Algebraic Geometry</label>
                                       <label><input type="radio"  id="math.AP" value="math.AP(Analysis of PDEs" v-model="SelectTopic"   >Analysis of PDEs</label>
                                       <label><input type="radio"  id="math.AT" value="math.AT(Algebraic Topology" v-model="SelectTopic"   >Algebraic Topology</label>
                                       <label><input type="radio"  id="math.CA" value="math.CA(Classical Analysis and ODEs" v-model="SelectTopic"   >Classical Analysis and ODEs</label>
                                       <label><input type="radio"  id="math.CO" value="math.CO(Combinatorics" v-model="SelectTopic"   ></label>
                                       <label><input type="radio"  id="math.CT" value="math.CT(Category Theory" v-model="SelectTopic"   >Category Theory</label>
                                       <label><input type="radio"  id="math.CV" value="math.CV(Complex Variables" v-model="SelectTopic"   >Complex Variables</label>
                                       <label><input type="radio"  id="math.DG" value="math.DG(Differential Geometry" v-model="SelectTopic"   >Differential Geometry</label>
                                       <label><input type="radio"  id="math.DS" value="math.DS(Dynamical Systems" v-model="SelectTopic"   >Dynamical Systems</label>
                                       <label><input type="radio"  id="math.FA" value="math.FA(Functional Analysis" v-model="SelectTopic"   >Functional Analysis</label>
                                       <label><input type="radio"  id="math.GM" value="math.GM(General Mathematics" v-model="SelectTopic"   >General Mathematics</label>
                                       <label><input type="radio"  id="math.GN" value="math.GN(General Topology" v-model="SelectTopic"   >General Topology</label>
                                       <label><input type="radio"  id="math.GR" value="math.GR(Group Theory" v-model="SelectTopic"   >Group Theory</label>
                                       <label><input type="radio"  id="math.GT" value="math.GT(Geometric Topology" v-model="SelectTopic"   >Geometric Topology</label>
                                       <label><input type="radio"  id="math.HO" value="math.HO(History and Overview" v-model="SelectTopic"   >History and Overview</label>
                                       <label><input type="radio"  id="math.IT" value="math.IT(Information Theory" v-model="SelectTopic"   >Information Theory</label>
                                       <label><input type="radio"  id="math.KT" value="math.KT(K-Theory and Homology" v-model="SelectTopic"   >K-Theory and Homology</label>
                                       <label><input type="radio"  id="math.LO" value="math.LO(Logic" v-model="SelectTopic"   >Logic</label>
                                       <label><input type="radio"  id="math.MG" value="math.MG(Metric Geometry" v-model="SelectTopic"   >Metric Geometry</label>
                                       <label><input type="radio"  id="math.MP" value="math.MP(Mathematical Physics" v-model="SelectTopic"   >Mathematical Physics</label>
                                       <label><input type="radio"  id="math.NA" value="math.NA(Numerical Analysis" v-model="SelectTopic"   >Numerical Analysis</label>
                                       <label><input type="radio"  id="math.NT" value="math.NT(Number Theory" v-model="SelectTopic"   >Number Theory</label>
                                       <label><input type="radio"  id="math.OA" value="math.OA(Operator Algebras" v-model="SelectTopic"   >Operator Algebras</label>
                                       <label><input type="radio"  id="math.OC" value="math.OC(Optimization and Control" v-model="SelectTopic"   >Optimization and Control</label>
                                       <label><input type="radio"  id="math.PR" value="math.PR(Probability" v-model="SelectTopic"   >Probability</label>
                                       <label><input type="radio"  id="math.QA" value="math.QA(Quantum Algebra" v-model="SelectTopic"   >Quantum Algebra</label>
                                       <label><input type="radio"  id="math.RA" value="math.RA(Rings and Algebras" v-model="SelectTopic"   >Rings and Algebras</label>
                                       <label><input type="radio"  id="math.RT" value="math.RT(Representation Theory" v-model="SelectTopic"   >Representation Theory</label>
                                       <label><input type="radio"  id="math.SG" value="math.SG(Symplectic Geometry" v-model="SelectTopic"   >Symplectic Geometry</label>
                                       <label><input type="radio"  id="math.SP" value="math.SP(Spectral Theory" v-model="SelectTopic"   >Spectral Theory</label>
                                       <label><input type="radio"  id="math.ST" value="math.ST(Statistics Theory" v-model="SelectTopic"   >Statistics Theory</label>

                                    </ol>
                                </details>


                                <details>
                                    <summary><strong>Physics</strong></summary>
                                    <ol>
                                       <label><input type="radio"  id="astro-ph.CO" value="astro-ph.CO(Cosmology and Nongalactic Astrophysics" v-model="SelectTopic"   >Cosmology and Nongalactic Astrophysics</label>
                                       <label><input type="radio"  id="astro-ph.EP" value="astro-ph.EP(Earth and Planetary Astrophysics" v-model="SelectTopic"   >Earth and Planetary Astrophysics</label>
                                       <label><input type="radio"  id="astro-ph.GA" value="astro-ph.GA(Astrophysics of Galaxies" v-model="SelectTopic"   >Astrophysics of Galaxies</label>
                                       <label><input type="radio"  id="astro-ph.HE" value="astro-ph.HE(High Energy Astrophysical Phenomena" v-model="SelectTopic"   >High Energy Astrophysical Phenomena</label>
                                       <label><input type="radio"  id="astro-ph.IM" value="astro-ph.IM(Instrumentation and Methods for Astrophysics" v-model="SelectTopic"   >Instrumentation and Methods for Astrophysics</label>
                                       <label><input type="radio"  id="astro-ph.SR" value="astro-ph.SR(Solar and Stellar Astrophysics" v-model="SelectTopic"   >Solar and Stellar Astrophysics</label>
                                       <label><input type="radio"  id="cond-mat.dis-nn" value="cond-mat.dis-nn(Disordered Systems and Neural Networks" v-model="SelectTopic"   >Disordered Systems and Neural Networks</label>
                                       <label><input type="radio"  id="marcond-mat.mes-hallk1" value="cond-mat.mes-hall(Mesoscale and Nanoscale Physics" v-model="SelectTopic"   >Mesoscale and Nanoscale Physics</label>
                                       <label><input type="radio"  id="cond-mat.mtrl-sci" value="cond-mat.mtrl-sci(Materials Science" v-model="SelectTopic"   >Materials Science</label>
                                       <label><input type="radio"  id="cond-mat.other" value="cond-mat.other(Other Condensed Matter" v-model="SelectTopic"   >Other Condensed Matter</label>
                                       <label><input type="radio"  id="cond-mat.quant-gas" value="cond-mat.quant-gas(Quantum Gases" v-model="SelectTopic"   >Quantum Gases</label>
                                       <label><input type="radio"  id="cond-mat.soft" value="cond-mat.soft(Soft Condensed Matter" v-model="SelectTopic"   >Soft Condensed Matter</label>
                                       <label><input type="radio"  id="cond-mat.stat-mech" value="cond-mat.stat-mech(Statistical Mechanics" v-model="SelectTopic"   >Statistical Mechanics</label>
                                       <label><input type="radio"  id="cond-mat.str-el" value="cond-mat.str-el(Strongly Correlated Electrons" v-model="SelectTopic"   >Strongly Correlated Electrons</label>
                                       <label><input type="radio"  id="cond-mat.supr-con" value="cond-mat.supr-con(Superconductivity" v-model="SelectTopic"   >Superconductivity</label>
                                       <label><input type="radio"  id="gr-qc" value="gr-qc(General Relativity and Quantum Cosmology" v-model="SelectTopic"   >General Relativity and Quantum Cosmology</label>
                                       <label><input type="radio"  id="hep-ex" value="hep-ex(High Energy Physics - Experiment" v-model="SelectTopic"   >High Energy Physics - Experiment</label>
                                       <label><input type="radio"  id="hep-lat" value="hep-lat(High Energy Physics - Lattice" v-model="SelectTopic"   >High Energy Physics - Lattice</label>
                                       <label><input type="radio"  id="hep-ph" value="hep-ph(High Energy Physics - Phenomenology" v-model="SelectTopic"   >High Energy Physics - Phenomenology</label>
                                       <label><input type="radio"  id="hep-th" value="hep-th(High Energy Physics - Theory" v-model="SelectTopic"   >High Energy Physics - Theory</label>
                                       <label><input type="radio"  id="math-ph" value="math-ph(Mathematical Physics" v-model="SelectTopic"   >Mathematical Physics</label>
                                       <label><input type="radio"  id="nlin.AO" value="nlin.AO(Adaptation and Self-Organizing Systems" v-model="SelectTopic"   >Adaptation and Self-Organizing Systems</label>
                                       <label><input type="radio"  id="nlin.CD" value="nlin.CD(Chaotic Dynamics" v-model="SelectTopic"   >Chaotic Dynamics</label>
                                       <label><input type="radio"  id="nlin.CG" value="nlin.CG(Cellular Automata and Lattice Gases" v-model="SelectTopic"   >Cellular Automata and Lattice Gases</label>
                                       <label><input type="radio"  id="nlin.PS" value="nlin.PS(Pattern Formation and Solitons" v-model="SelectTopic"   >Pattern Formation and Solitons</label>
                                       <label><input type="radio"  id="nlin.SI" value="nlin.SI(Exactly Solvable and Integrable Systems" v-model="SelectTopic"   >Exactly Solvable and Integrable Systems</label>
                                       <label><input type="radio"  id="nucl-ex" value="nucl-ex(Nuclear Experiment" v-model="SelectTopic"   >Nuclear Experiment</label>
                                       <label><input type="radio"  id="nucl-th" value="nucl-th(Nuclear Theory" v-model="SelectTopic"   >Nuclear Theory</label>
                                       <label><input type="radio"  id="physics.ao-ph" value="physics.ao-ph(Atmospheric and Oceanic Physics" v-model="SelectTopic"   >Atmospheric and Oceanic Physics</label>
                                       <label><input type="radio"  id="physics.app-ph" value="physics.app-ph(Applied Physics" v-model="SelectTopic"   >Applied Physics</label>
                                       <label><input type="radio"  id="physics.atm-clus" value="physics.atm-clus(Atomic and Molecular Clusters" v-model="SelectTopic"   >Atomic and Molecular Clusters</label>
                                       <label><input type="radio"  id="physics.atom-ph" value="physics.atom-ph(Atomic Physics" v-model="SelectTopic"   >Atomic Physics</label>
                                       <label><input type="radio"  id="physics.bio-ph" value="physics.bio-ph(Biological Physics" v-model="SelectTopic"   >Biological Physics</label>
                                       <label><input type="radio"  id="physics.chem-ph" value="physics.chem-ph(Chemical Physics" v-model="SelectTopic"   >Chemical Physics</label>
                                       <label><input type="radio"  id="physics.class-ph" value="physics.class-ph(Classical Physics" v-model="SelectTopic"   >Classical Physics</label>
                                       <label><input type="radio"  id="physics.comp-ph" value="physics.comp-ph(Computational Physics" v-model="SelectTopic"   >Computational Physics</label>
                                       <label><input type="radio"  id="physics.data-an" value="physics.data-an(Data Analysis Statistics and Probability" v-model="SelectTopic"   >Data Analysis Statistics and Probability</label>
                                       <label><input type="radio"  id="physics.ed-ph" value="physics.ed-ph(Physics Education" v-model="SelectTopic"   >Physics Education</label>
                                       <label><input type="radio"  id="physics.flu-dyn" value="physics.flu-dyn(Fluid Dynamics" v-model="SelectTopic"   >Fluid Dynamics</label>
                                       <label><input type="radio"  id="physics.gen-ph" value="physics.gen-ph(General Physics" v-model="SelectTopic"   >General Physics</label>
                                       <label><input type="radio"  id="physics.geo-ph" value="physics.geo-ph(Geophysics" v-model="SelectTopic"   >Geophysics</label>
                                       <label><input type="radio"  id="physics.hist-ph" value="physics.hist-ph(History and Philosophy of Physics" v-model="SelectTopic"   >History and Philosophy of Physics</label>
                                       <label><input type="radio"  id="physics.ins-det" value="physics.ins-det(Instrumentation and Detectors" v-model="SelectTopic"   >Instrumentation and Detectors</label>
                                       <label><input type="radio"  id="physics.med-ph" value="physics.med-ph(Medical Physics" v-model="SelectTopic"   >Medical Physics</label>
                                       <label><input type="radio"  id="physics.optics" value="physics.optics(Optics" v-model="SelectTopic"   >Optics</label>
                                       <label><input type="radio"  id="physics.plasm-ph" value="physics.plasm-ph(Plasma Physics" v-model="SelectTopic"   >Plasma Physics</label>
                                       <label><input type="radio"  id="physics.pop-ph" value="physics.pop-ph(Popular Physics" v-model="SelectTopic"   >Popular Physics</label>
                                       <label><input type="radio"  id="physics.soc-ph" value="physics.soc-ph(Physics and Society" v-model="SelectTopic"   >Physics and Society</label>
                                       <label><input type="radio"  id="physics.space-ph" value="physics.space-ph(Space Physics" v-model="SelectTopic"   >Space Physics</label>
                                       <label><input type="radio"  id="quant-ph" value="quant-ph(Quantum Physics" v-model="SelectTopic"   >Quantum Physics</label>

                                    </ol>
                                </details>


                                <details>
                                    <summary><strong>Quantitative Biology</strong></summary>
                                    <ol>

                                       <label><input type="radio"  id="q-bio.CB" value="q-bio.CB(Cell Behavior" v-model="SelectTopic"   >Cell Behavior</label>
                                       <label><input type="radio"  id="q-bio.GN" value="q-bio.GN(Genomics" v-model="SelectTopic"   >Genomics</label>
                                       <label><input type="radio"  id="q-bio.MN" value="q-bio.MN(Molecular Networks" v-model="SelectTopic"   >Molecular Networks</label>
                                       <label><input type="radio"  id="q-bio.NC" value="q-bio.NC(Neurons and Cognition" v-model="SelectTopic"   >Neurons and Cognition</label>
                                       <label><input type="radio"  id="q-bio.OT" value="q-bio.OT(Other Quantitative Biology" v-model="SelectTopic"   >Other Quantitative Biology</label>
                                       <label><input type="radio"  id="q-bio.PE" value="q-bio.PE(Populations and Evolution" v-model="SelectTopic"   >Populations and Evolution</label>
                                       <label><input type="radio"  id="q-bio.QM" value="q-bio.QM(Quantitative Methods" v-model="SelectTopic"   >Quantitative Methods</label>
                                       <label><input type="radio"  id="q-bio.SC" value="q-bio.SC(Subcellular Processes" v-model="SelectTopic"   >Subcellular Processes</label>
                                       <label><input type="radio"  id="q-bio.TO" value="q-bio.TO(Tissues and Organs" v-model="SelectTopic"   >Tissues and Organs</label>


                                    </ol>
                                </details>

                                <details>
                                    <summary><strong>Quantitative Finance</strong></summary>
                                    <ol>
                                       <label><input type="radio"  id="q-fin.CP" value="q-fin.CP(Computational Finance" v-model="SelectTopic"   >Computational Finance</label>
                                       <label><input type="radio"  id="q-fin.EC" value="q-fin.EC(Economics" v-model="SelectTopic"   >Economics</label>
                                       <label><input type="radio"  id="q-fin.GN" value="q-fin.GN(General Finance" v-model="SelectTopic"   >General Finance</label>
                                       <label><input type="radio"  id="q-fin.MF" value="q-fin.MF(Mathematical Finance" v-model="SelectTopic"   >Mathematical Finance</label>
                                       <label><input type="radio"  id="q-fin.PM" value="q-fin.PM(Portfolio Management" v-model="SelectTopic"   >Portfolio Management</label>
                                       <label><input type="radio"  id="q-fin.PR" value="q-fin.PR(Pricing of Securities" v-model="SelectTopic"   >Pricing of Securities</label>
                                       <label><input type="radio"  id="q-fin.RM" value="q-fin.RM(Risk Management" v-model="SelectTopic"   >Risk Management</label>
                                       <label><input type="radio"  id="q-fin.ST" value="q-fin.ST(Statistical Finance" v-model="SelectTopic"   >Statistical Finance</label>
                                       <label><input type="radio"  id="q-fin.TR" value="q-fin.TR(Trading and Market Microstructure" v-model="SelectTopic"   >Trading and Market Microstructure</label>
                                    </ol>
                                </details>

                                <details>
                                    <summary><strong>Statistics</strong></summary>
                                    <ol>
                                       <label><input type="radio"  id="stat.AP" value="stat.AP(Applications" v-model="SelectTopic"   >Applications</label>
                                       <label><input type="radio"  id="stat.CO" value="stat.CO(Computation" v-model="SelectTopic"   >Computation</label>
                                       <label><input type="radio"  id="stat.ME" value="stat.ME(Methodology" v-model="SelectTopic"   >Methodology</label>
                                       <label><input type="radio"  id="stat.ML" value="stat.ML(Machine Learning" v-model="SelectTopic"   >Machine Learning</label>
                                       <label><input type="radio"  id="stat.OT" value="stat.OT(Other Statistics" v-model="SelectTopic"   >Other Statistics</label>
                                       <label><input type="radio"  id="stat.TH" value="stat.TH(Statistics Theory" v-model="SelectTopic"   >Statistics Theory</label>
                                    </ol>
                                </details>


                               
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
