
<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, ref } from 'vue'
import PaperRecommend from '../components/PaperRecommend.vue';
import router from '../router'







export default {
    name: 'PaperView',
    components: {
        PaperRecommend
    },


    setup() {


    }
}
</script>


<template>

   



    <div class="content">
      <nav class="pagination is-small is-centered breathe-horizontal" role="navigation" aria-label="pagination">
        
        <a href="" class="pagination-previous is-invisible">Previous
        </a>
        
        
          <a href="/search/?query=tacotron&amp;searchtype=all&amp;source=header&amp;order=-announced_date_first&amp;size=50&amp;abstracts=show&amp;start=50" class="pagination-next">Next
          </a>
        
        <ul class="pagination-list">
    
          <li>
            <a href="/search/?query=tacotron&amp;searchtype=all&amp;source=header&amp;order=-announced_date_first&amp;size=50&amp;abstracts=show&amp;start=0" class="pagination-link is-current" aria-label="Goto page 1">1
            </a>
          </li>
    
          
            
            <li>
              <a href="/search/?query=tacotron&amp;searchtype=all&amp;source=header&amp;order=-announced_date_first&amp;size=50&amp;abstracts=show&amp;start=50" class="pagination-link " aria-label="Page 2" aria-current="page">2
              </a>
            </li>
            
          
        </ul>
      </nav>
      
    
    
    
    <ol class="breathe-horizontal" start="1"> 
    
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2209.14698">arXiv:2209.14698</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2209.14698">pdf</a>, <a href="https://arxiv.org/format/2209.14698">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Computer Vision and Pattern Recognition">cs.CV</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Networking and Internet Architecture">cs.NI</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Social and Information Networks">cs.SI</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Facial Landmark Predictions with Applications to Metaverse
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Han%2C+Q">Qiao Han</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhao%2C+J">Jun Zhao</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Lam%2C+K">Kwok-Yan Lam</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2209.14698v1-abstract-short" style="display: inline;">
            This research aims to make metaverse characters more realistic by adding lip animations learnt from videos in the wild. To achieve this, our approach is to extend <span class="search-hit mathjax">Tacotron</span> 2 text-to-speech synthesizer to generate lip movements together with mel spectrogram in one pass. The encoder and gate layer weights are pre-trained on LJ Speech 1.1 data set while the dec…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2209.14698v1-abstract-full').style.display = 'inline'; document.getElementById('2209.14698v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2209.14698v1-abstract-full" style="display: none;">
            This research aims to make metaverse characters more realistic by adding lip animations learnt from videos in the wild. To achieve this, our approach is to extend <span class="search-hit mathjax">Tacotron</span> 2 text-to-speech synthesizer to generate lip movements together with mel spectrogram in one pass. The encoder and gate layer weights are pre-trained on LJ Speech 1.1 data set while the decoder is retrained on 93 clips of TED talk videos extracted from LRS 3 data set. Our novel decoder predicts displacement in 20 lip landmark positions across time, using labels automatically extracted by OpenFace 2.0 landmark predictor. Training converged in 7 hours using less than 5 minutes of video. We conducted ablation study for Pre/Post-Net and pre-trained encoder weights to demonstrate the effectiveness of transfer learning between audio and visual speech data.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2209.14698v1-abstract-full').style.display = 'none'; document.getElementById('2209.14698v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 29 September, 2022; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> September 2022.
          
        </p>
        
    
        
          <p class="comments is-size-7">
            
              <span class="has-text-black-bis has-text-weight-semibold">Report number:</span>
              This paper appears in the Proceedings of 2022 IEEE 8th World Forum on Internet of Things (WF-IoT). Please feel free to contact us for questions or remarks
            
    
            
    
            
          </p>
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2208.13183">arXiv:2208.13183</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2208.13183">pdf</a>, <a href="https://arxiv.org/format/2208.13183">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Training Text-To-Speech Systems From Synthetic Data: A Practical Approach For Accent Transfer Tasks
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Finkelstein%2C+L">Lev Finkelstein</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zen%2C+H">Heiga Zen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Casagrande%2C+N">Norman Casagrande</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chan%2C+C">Chun-an Chan</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Jia%2C+Y">Ye Jia</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Kenter%2C+T">Tom Kenter</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Petelin%2C+A">Alexey Petelin</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Shen%2C+J">Jonathan Shen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wan%2C+V">Vincent Wan</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+Y">Yu Zhang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wu%2C+Y">Yonghui Wu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Clark%2C+R">Rob Clark</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2208.13183v1-abstract-short" style="display: inline;">
            …on data generated by a less robust TTS system designed for a high-quality transfer task; in particular, a CHiVE-BERT monolingual TTS system is trained on the output of a <span class="search-hit mathjax">Tacotron</span> model designed for accent transfer. While some quality loss is inevitable with this approach, experimental results show that the models trained on synthetic data this way can produc…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2208.13183v1-abstract-full').style.display = 'inline'; document.getElementById('2208.13183v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2208.13183v1-abstract-full" style="display: none;">
            Transfer tasks in text-to-speech (TTS) synthesis - where one or more aspects of the speech of one set of speakers is transferred to another set of speakers that do not feature these aspects originally - remains a challenging task. One of the challenges is that models that have high-quality transfer capabilities can have issues in stability, making them impractical for user-facing critical tasks. This paper demonstrates that transfer can be obtained by training a robust TTS system on data generated by a less robust TTS system designed for a high-quality transfer task; in particular, a CHiVE-BERT monolingual TTS system is trained on the output of a <span class="search-hit mathjax">Tacotron</span> model designed for accent transfer. While some quality loss is inevitable with this approach, experimental results show that the models trained on synthetic data this way can produce high quality audio displaying accent transfer, while preserving speaker characteristics such as speaking style.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2208.13183v1-abstract-full').style.display = 'none'; document.getElementById('2208.13183v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 28 August, 2022; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2022.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">To be published in Interspeech 2022</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2206.07373">arXiv:2206.07373</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2206.07373">pdf</a>, <a href="https://arxiv.org/format/2206.07373">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            NatiQ: An End-to-end Text-to-Speech System for Arabic
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Abdelali%2C+A">Ahmed Abdelali</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Durrani%2C+N">Nadir Durrani</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Demiroglu%2C+C">Cenk Demiroglu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Dalvi%2C+F">Fahim Dalvi</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Mubarak%2C+H">Hamdy Mubarak</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Darwish%2C+K">Kareem Darwish</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2206.07373v1-abstract-short" style="display: inline;">
            NatiQ is end-to-end text-to-speech system for Arabic. Our speech synthesizer uses an encoder-decoder architecture with attention. We used both <span class="search-hit mathjax">tacotron</span>-based models (<span class="search-hit mathjax">tacotron</span>-1 and <span class="search-hit mathjax">tacotron</span>-2) and the faster transformer model for generating mel-spectrograms from characters. We co…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2206.07373v1-abstract-full').style.display = 'inline'; document.getElementById('2206.07373v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2206.07373v1-abstract-full" style="display: none;">
            NatiQ is end-to-end text-to-speech system for Arabic. Our speech synthesizer uses an encoder-decoder architecture with attention. We used both <span class="search-hit mathjax">tacotron</span>-based models (<span class="search-hit mathjax">tacotron</span>-1 and <span class="search-hit mathjax">tacotron</span>-2) and the faster transformer model for generating mel-spectrograms from characters. We concatenated Tacotron1 with the WaveRNN vocoder, Tacotron2 with the WaveGlow vocoder and ESPnet transformer with the parallel wavegan vocoder to synthesize waveforms from the spectrograms. We used in-house speech data for two voices: 1) neutral male "Hamza"- narrating general content and news, and 2) expressive female "Amina"- narrating children story books to train our models. Our best systems achieve an average Mean Opinion Score (MOS) of 4.21 and 4.40 for Amina and Hamza respectively. The objective evaluation of the systems using word and character error rate (WER and CER) as well as the response time measured by real-time factor favored the end-to-end architecture ESPnet. NatiQ demo is available on-line at https://tts.qcri.org
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2206.07373v1-abstract-full').style.display = 'none'; document.getElementById('2206.07373v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 15 June, 2022; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> June 2022.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2204.04127">arXiv:2204.04127</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2204.04127">pdf</a>, <a href="https://arxiv.org/format/2204.04127">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
            
              <div class="is-inline-block" style="margin-left: 0.5rem">
                <div class="tags has-addons">
                  <span class="tag is-dark is-size-7">doi</span>
                  <span class="tag is-light is-size-7"><a class="" href="https://doi.org/10.21437/Interspeech.2022-10446">10.21437/Interspeech.2022-10446 <i class="fa fa-external-link" aria-hidden="true"></i></a></span>
                </div>
              </div>
            
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Karaoker: Alignment-free singing voice synthesis with speech training data
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Kakoulidis%2C+P">Panos Kakoulidis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ellinas%2C+N">Nikolaos Ellinas</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Vamvoukakis%2C+G">Georgios Vamvoukakis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Markopoulos%2C+K">Konstantinos Markopoulos</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Sung%2C+J+S">June Sig Sung</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Jho%2C+G">Gunu Jho</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Tsiakoulis%2C+P">Pirros Tsiakoulis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chalamandaris%2C+A">Aimilios Chalamandaris</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2204.04127v2-abstract-short" style="display: inline;">
            …on singing data and depend on either error-prone time-alignment and duration features or explicit music score information. In this paper, we propose Karaoker, a multispeaker <span class="search-hit mathjax">Tacotron</span>-based model conditioned on voice characteristic features that is trained exclusively on spoken data without requiring time-alignments. Karaoker synthesizes singing voice and tra…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2204.04127v2-abstract-full').style.display = 'inline'; document.getElementById('2204.04127v2-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2204.04127v2-abstract-full" style="display: none;">
            Existing singing voice synthesis models (SVS) are usually trained on singing data and depend on either error-prone time-alignment and duration features or explicit music score information. In this paper, we propose Karaoker, a multispeaker <span class="search-hit mathjax">Tacotron</span>-based model conditioned on voice characteristic features that is trained exclusively on spoken data without requiring time-alignments. Karaoker synthesizes singing voice and transfers style following a multi-dimensional template extracted from a source waveform of an unseen singer/speaker. The model is jointly conditioned with a single deep convolutional encoder on continuous data including pitch, intensity, harmonicity, formants, cepstral peak prominence and octaves. We extend the text-to-speech training objective with feature reconstruction, classification and speaker identification tasks that guide the model to an accurate result. In addition to multitasking, we also employ a Wasserstein GAN training scheme as well as new losses on the acoustic model's output to further refine the quality of the model.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2204.04127v2-abstract-full').style.display = 'none'; document.getElementById('2204.04127v2-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 31 August, 2022; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 8 April, 2022;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> April 2022.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Accepted to INTERSPEECH 2022</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2204.03421">arXiv:2204.03421</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2204.03421">pdf</a>, <a href="https://arxiv.org/ps/2204.03421">ps</a>, <a href="https://arxiv.org/format/2204.03421">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Self supervised learning for robust voice cloning
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Klapsas%2C+K">Konstantinos Klapsas</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ellinas%2C+N">Nikolaos Ellinas</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Nikitaras%2C+K">Karolos Nikitaras</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Vamvoukakis%2C+G">Georgios Vamvoukakis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Kakoulidis%2C+P">Panos Kakoulidis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Markopoulos%2C+K">Konstantinos Markopoulos</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Raptis%2C+S">Spyros Raptis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Sung%2C+J+S">June Sig Sung</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Jho%2C+G">Gunu Jho</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chalamandaris%2C+A">Aimilios Chalamandaris</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Tsiakoulis%2C+P">Pirros Tsiakoulis</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2204.03421v1-abstract-short" style="display: inline;">
            …identity and to make them robust to noise and acoustic conditions. The learned features are used as pre-trained utterance-level embeddings and as inputs to a Non-Attentive <span class="search-hit mathjax">Tacotron</span> based architecture, aiming to achieve multispeaker speech synthesis without utilizing additional speaker features. This method enables us to train our model in an unlabeled multis…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2204.03421v1-abstract-full').style.display = 'inline'; document.getElementById('2204.03421v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2204.03421v1-abstract-full" style="display: none;">
            Voice cloning is a difficult task which requires robust and informative features incorporated in a high quality TTS system in order to effectively copy an unseen speaker's voice. In our work, we utilize features learned in a self-supervised framework via the Bootstrap Your Own Latent (BYOL) method, which is shown to produce high quality speech representations when specific audio augmentations are applied to the vanilla algorithm. We further extend the augmentations in the training procedure to aid the resulting features to capture the speaker identity and to make them robust to noise and acoustic conditions. The learned features are used as pre-trained utterance-level embeddings and as inputs to a Non-Attentive <span class="search-hit mathjax">Tacotron</span> based architecture, aiming to achieve multispeaker speech synthesis without utilizing additional speaker features. This method enables us to train our model in an unlabeled multispeaker dataset as well as use unseen speaker embeddings to copy a speaker's voice. Subjective and objective evaluations are used to validate the proposed model, as well as the robustness to the acoustic conditions of the target utterance.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2204.03421v1-abstract-full').style.display = 'none'; document.getElementById('2204.03421v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 7 April, 2022; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> April 2022.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Submitted to INTERSPEECH 2022</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2204.01115">arXiv:2204.01115</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2204.01115">pdf</a>, <a href="https://arxiv.org/format/2204.01115">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Human-Computer Interaction">cs.HC</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            On incorporating social speaker characteristics in synthetic speech
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Rallabandi%2C+S+S">Sai Sirisha Rallabandi</a>, 
          
          <a href="/search/?searchtype=author&amp;query=M%C3%B6ller%2C+S">Sebastian Möller</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2204.01115v1-abstract-short" style="display: inline;">
            …convex combinations were investigated for the generation of higher competence in female speech. We have employed a feature quantization approach in the traditional end-to-end <span class="search-hit mathjax">tacotron</span> based speech synthesis model. The listening tests have shown that the convex combination of acoustic features displays higher Mean Opinion Scores of warmth and competence when…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2204.01115v1-abstract-full').style.display = 'inline'; document.getElementById('2204.01115v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2204.01115v1-abstract-full" style="display: none;">
            In our previous work, we derived the acoustic features, that contribute to the perception of warmth and competence in synthetic speech. As an extension, in our current work, we investigate the impact of the derived vocal features in the generation of the desired characteristics. The acoustic features, spectral flux, F1 mean and F2 mean and their convex combinations were explored for the generation of higher warmth in female speech. The voiced slope, spectral flux, and their convex combinations were investigated for the generation of higher competence in female speech. We have employed a feature quantization approach in the traditional end-to-end <span class="search-hit mathjax">tacotron</span> based speech synthesis model. The listening tests have shown that the convex combination of acoustic features displays higher Mean Opinion Scores of warmth and competence when compared to that of individual features.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2204.01115v1-abstract-full').style.display = 'none'; document.getElementById('2204.01115v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 3 April, 2022; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> April 2022.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Submitted to Interspeech 2022</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2203.02967">arXiv:2203.02967</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2203.02967">pdf</a>, <a href="https://arxiv.org/format/2203.02967">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Variational Auto-Encoder based Mandarin Speech Cloning
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Xing%2C+Q">Qingyu Xing</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ma%2C+X">Xiaohan Ma</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2203.02967v1-abstract-short" style="display: inline;">
            …However, because of prosodic phrasing and large character set of Mandarin, Chinese utilization of these models is not yet complete. By creating a new dataset and replacing <span class="search-hit mathjax">Tacotron</span> synthesizer with VAENAR-TTS, we improved the existing speech cloning technique CV2TTS to almost real-time speech cloning while guaranteeing synthesis quality. In the process, we…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2203.02967v1-abstract-full').style.display = 'inline'; document.getElementById('2203.02967v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2203.02967v1-abstract-full" style="display: none;">
            Speech cloning technology is becoming more sophisticated thanks to the advances in machine learning. Researchers have successfully implemented natural-sounding English speech synthesis and good English speech cloning by some effective models. However, because of prosodic phrasing and large character set of Mandarin, Chinese utilization of these models is not yet complete. By creating a new dataset and replacing <span class="search-hit mathjax">Tacotron</span> synthesizer with VAENAR-TTS, we improved the existing speech cloning technique CV2TTS to almost real-time speech cloning while guaranteeing synthesis quality. In the process, we customized the subjective tests of synthesis quality assessment by attaching various scenarios, so that subjects focus on the differences between voice and our improvements maybe were more advantageous to practical applications. The results of the A/B test, real-time factor (RTF) and 2.74 mean opinion score (MOS) in terms of naturalness and similarity, reflect the real-time high-quality Mandarin speech cloning we achieved.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2203.02967v1-abstract-full').style.display = 'none'; document.getElementById('2203.02967v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 6 March, 2022; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> March 2022.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Submitted to Insterspeech 2022</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2202.07907">arXiv:2202.07907</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2202.07907">pdf</a>, <a href="https://arxiv.org/format/2202.07907">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Singing-<span class="search-hit mathjax">Tacotron</span>: Global duration control attention and dynamic filter for End-to-end singing voice synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Wang%2C+T">Tao Wang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Fu%2C+R">Ruibo Fu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Yi%2C+J">Jiangyan Yi</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Tao%2C+J">Jianhua Tao</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wen%2C+Z">Zhengqi Wen</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2202.07907v1-abstract-short" style="display: inline;">
            …model instability or even failure to synthesize voice. To learn accurate alignment information automatically, this paper proposes an end-to-end SVS framework, named Singing-<span class="search-hit mathjax">Tacotron</span>. The main difference between the proposed framework and <span class="search-hit mathjax">Tacotron</span> is that the speech can be controlled significantly by the musical score&amp;#…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2202.07907v1-abstract-full').style.display = 'inline'; document.getElementById('2202.07907v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2202.07907v1-abstract-full" style="display: none;">
            End-to-end singing voice synthesis (SVS) is attractive due to the avoidance of pre-aligned data. However, the auto learned alignment of singing voice with lyrics is difficult to match the duration information in musical score, which will lead to the model instability or even failure to synthesize voice. To learn accurate alignment information automatically, this paper proposes an end-to-end SVS framework, named Singing-<span class="search-hit mathjax">Tacotron</span>. The main difference between the proposed framework and <span class="search-hit mathjax">Tacotron</span> is that the speech can be controlled significantly by the musical score's duration information. Firstly, we propose a global duration control attention mechanism for the SVS model. The attention mechanism can control each phoneme's duration. Secondly, a duration encoder is proposed to learn a set of global transition tokens from the musical score. These transition tokens can help the attention mechanism decide whether moving to the next phoneme or staying at each decoding step. Thirdly, to further improve the model's stability, a dynamic filter is designed to help the model overcome noise interference and pay more attention to local context information. Subjective and objective evaluation verify the effectiveness of the method. Furthermore, the role of global transition tokens and the effect of duration control are explored. Examples of experiments can be found at https://hairuo55.github.io/SingingTacotron.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2202.07907v1-abstract-full').style.display = 'none'; document.getElementById('2202.07907v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 16 February, 2022; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> February 2022.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">5 pages, 7 figures</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2201.12567">arXiv:2201.12567</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2201.12567">pdf</a>, <a href="https://arxiv.org/format/2201.12567">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            The HCCL-DKU system for fake audio generation task of the 2022 ICASSP ADD Challenge
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Chen%2C+Z">Ziyi Chen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Hua%2C+H">Hua Hua</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+Y">Yuxiang Zhang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+M">Ming Li</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+P">Pengyuan Zhang</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2201.12567v1-abstract-short" style="display: inline;">
            …ppg-based voice conversion model that adopts a fully end-to-end structure. Experimental results show that the proposed method outperforms other conversion models, including <span class="search-hit mathjax">Tacotron</span>-based and Fastspeech-based models, on conversion quality and spoofing performance against anti-spoofing systems. In addition, we investigate several post-processing methods for b…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2201.12567v1-abstract-full').style.display = 'inline'; document.getElementById('2201.12567v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2201.12567v1-abstract-full" style="display: none;">
            The voice conversion task is to modify the speaker identity of continuous speech while preserving the linguistic content. Generally, the naturalness and similarity are two main metrics for evaluating the conversion quality, which has been improved significantly in recent years. This paper presents the HCCL-DKU entry for the fake audio generation task of the 2022 ICASSP ADD challenge. We propose a novel ppg-based voice conversion model that adopts a fully end-to-end structure. Experimental results show that the proposed method outperforms other conversion models, including <span class="search-hit mathjax">Tacotron</span>-based and Fastspeech-based models, on conversion quality and spoofing performance against anti-spoofing systems. In addition, we investigate several post-processing methods for better spoofing power. Finally, we achieve second place with a deception success rate of 0.916 in the ADD challenge.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2201.12567v1-abstract-full').style.display = 'none'; document.getElementById('2201.12567v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 29 January, 2022; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> January 2022.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2201.10375">arXiv:2201.10375</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2201.10375">pdf</a>, <a href="https://arxiv.org/format/2201.10375">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Zero-Shot Long-Form Voice Cloning with Dynamic Convolution Attention
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Gorodetskii%2C+A">Artem Gorodetskii</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ozhiganov%2C+I">Ivan Ozhiganov</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2201.10375v2-abstract-short" style="display: inline;">
            …is realized using an energy-based attention mechanism known as Dynamic Convolution Attention, in combination with a set of modifications proposed for the synthesizer based on <span class="search-hit mathjax">Tacotron</span> 2. Moreover, effective zero-shot speaker adaptation is achieved by conditioning both the synthesizer and vocoder on a speaker encoder that has been pretrained on a large corpus…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2201.10375v2-abstract-full').style.display = 'inline'; document.getElementById('2201.10375v2-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2201.10375v2-abstract-full" style="display: none;">
            With recent advancements in voice cloning, the performance of speech synthesis for a target speaker has been rendered similar to the human level. However, autoregressive voice cloning systems still suffer from text alignment failures, resulting in an inability to synthesize long sentences. In this work, we propose a variant of attention-based text-to-speech system that can reproduce a target voice from a few seconds of reference speech and generalize to very long utterances as well. The proposed system is based on three independently trained components: a speaker encoder, synthesizer and universal vocoder. Generalization to long utterances is realized using an energy-based attention mechanism known as Dynamic Convolution Attention, in combination with a set of modifications proposed for the synthesizer based on <span class="search-hit mathjax">Tacotron</span> 2. Moreover, effective zero-shot speaker adaptation is achieved by conditioning both the synthesizer and vocoder on a speaker encoder that has been pretrained on a large corpus of diverse data. We compare several implementations of voice cloning systems in terms of speech naturalness, speaker similarity, alignment consistency and ability to synthesize long utterances, and conclude that the proposed model can produce intelligible synthetic speech for extremely long utterances, while preserving a high extent of naturalness and similarity for short texts.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2201.10375v2-abstract-full').style.display = 'none'; document.getElementById('2201.10375v2-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 26 January, 2022; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 25 January, 2022;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> January 2022.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Added article structure</span>
        </p>
        
    
        
          <p class="comments is-size-7">
            
    
            
    
            
              <span class="has-text-black-bis has-text-weight-semibold">ACM Class:</span>
              I.2.7
            
          </p>
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2111.10173">arXiv:2111.10173</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2111.10173">pdf</a>, <a href="https://arxiv.org/format/2111.10173">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
            
              <div class="is-inline-block" style="margin-left: 0.5rem">
                <div class="tags has-addons">
                  <span class="tag is-dark is-size-7">doi</span>
                  <span class="tag is-light is-size-7"><a class="" href="https://doi.org/10.1007/978-3-030-87802-3_31">10.1007/978-3-030-87802-3_31 <i class="fa fa-external-link" aria-hidden="true"></i></a></span>
                </div>
              </div>
            
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Word-Level Style Control for Expressive, Non-attentive Speech Synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Klapsas%2C+K">Konstantinos Klapsas</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ellinas%2C+N">Nikolaos Ellinas</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Sung%2C+J+S">June Sig Sung</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Park%2C+H">Hyoungmin Park</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Raptis%2C+S">Spyros Raptis</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2111.10173v1-abstract-short" style="display: inline;">
            …order to disentangle it from the style information. The two encoder outputs are aligned and concatenated with the phoneme encoder outputs and then decoded with a Non-Attentive <span class="search-hit mathjax">Tacotron</span> model. An extra prior encoder is used to predict the style tokens autoregressively, in order for the model to be able to run without a reference utterance. We find that the re…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2111.10173v1-abstract-full').style.display = 'inline'; document.getElementById('2111.10173v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2111.10173v1-abstract-full" style="display: none;">
            This paper presents an expressive speech synthesis architecture for modeling and controlling the speaking style at a word level. It attempts to learn word-level stylistic and prosodic representations of the speech data, with the aid of two encoders. The first one models style by finding a combination of style tokens for each word given the acoustic features, and the second outputs a word-level sequence conditioned only on the phonetic information in order to disentangle it from the style information. The two encoder outputs are aligned and concatenated with the phoneme encoder outputs and then decoded with a Non-Attentive <span class="search-hit mathjax">Tacotron</span> model. An extra prior encoder is used to predict the style tokens autoregressively, in order for the model to be able to run without a reference utterance. We find that the resulting model gives both word-level and global control over the style, as well as prosody transfer capabilities.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2111.10173v1-abstract-full').style.display = 'none'; document.getElementById('2111.10173v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 19 November, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> November 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Proceedings of SPECOM 2021</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2111.09146">arXiv:2111.09146</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2111.09146">pdf</a>, <a href="https://arxiv.org/format/2111.09146">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
            
              <div class="is-inline-block" style="margin-left: 0.5rem">
                <div class="tags has-addons">
                  <span class="tag is-dark is-size-7">doi</span>
                  <span class="tag is-light is-size-7"><a class="" href="https://doi.org/10.21437/SSW.2021-21">10.21437/SSW.2021-21 <i class="fa fa-external-link" aria-hidden="true"></i></a></span>
                </div>
              </div>
            
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Rapping-Singing Voice Synthesis based on Phoneme-level Prosody Control
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Markopoulos%2C+K">Konstantinos Markopoulos</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ellinas%2C+N">Nikolaos Ellinas</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Vioni%2C+A">Alexandra Vioni</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Christidou%2C+M">Myrsini Christidou</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Kakoulidis%2C+P">Panos Kakoulidis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Vamvoukakis%2C+G">Georgios Vamvoukakis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Maniati%2C+G">Georgia Maniati</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Sung%2C+J+S">June Sig Sung</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Park%2C+H">Hyoungmin Park</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Tsiakoulis%2C+P">Pirros Tsiakoulis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chalamandaris%2C+A">Aimilios Chalamandaris</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2111.09146v1-abstract-short" style="display: inline;">
            In this paper, a text-to-rapping/singing system is introduced, which can be adapted to any speaker's voice. It utilizes a <span class="search-hit mathjax">Tacotron</span>-based multispeaker acoustic model trained on read-only speech data and which provides prosody control at the phoneme level. Dataset augmentation and additional prosody manipulation based on traditional DSP algorithms are also…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2111.09146v1-abstract-full').style.display = 'inline'; document.getElementById('2111.09146v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2111.09146v1-abstract-full" style="display: none;">
            In this paper, a text-to-rapping/singing system is introduced, which can be adapted to any speaker's voice. It utilizes a <span class="search-hit mathjax">Tacotron</span>-based multispeaker acoustic model trained on read-only speech data and which provides prosody control at the phoneme level. Dataset augmentation and additional prosody manipulation based on traditional DSP algorithms are also investigated. The neural TTS model is fine-tuned to an unseen speaker's limited recordings, allowing rapping/singing synthesis with the target's speaker voice. The detailed pipeline of the system is described, which includes the extraction of the target pitch and duration values from an a capella song and their conversion into target speaker's valid range of notes before synthesis. An additional stage of prosodic manipulation of the output via WSOLA is also investigated for better matching the target duration values. The synthesized utterances can be mixed with an instrumental accompaniment track to produce a complete song. The proposed system is evaluated via subjective listening tests as well as in comparison to an available alternate system which also aims to produce synthetic singing voice from read-only training data. Results show that the proposed approach can produce high quality rapping/singing voice with increased naturalness.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2111.09146v1-abstract-full').style.display = 'none'; document.getElementById('2111.09146v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 17 November, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> November 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Proceedings of 11th ISCA Speech Synthesis Workshop (SSW 11)</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2111.09052">arXiv:2111.09052</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2111.09052">pdf</a>, <a href="https://arxiv.org/format/2111.09052">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
            
              <div class="is-inline-block" style="margin-left: 0.5rem">
                <div class="tags has-addons">
                  <span class="tag is-dark is-size-7">doi</span>
                  <span class="tag is-light is-size-7"><a class="" href="https://doi.org/10.21437/Interspeech.2020-2464">10.21437/Interspeech.2020-2464 <i class="fa fa-external-link" aria-hidden="true"></i></a></span>
                </div>
              </div>
            
          
        </div>
        
        <p class="title is-5 mathjax">
          
            High Quality Streaming Speech Synthesis with Low, Sentence-Length-Independent Latency
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Ellinas%2C+N">Nikolaos Ellinas</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Vamvoukakis%2C+G">Georgios Vamvoukakis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Markopoulos%2C+K">Konstantinos Markopoulos</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chalamandaris%2C+A">Aimilios Chalamandaris</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Maniati%2C+G">Georgia Maniati</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Kakoulidis%2C+P">Panos Kakoulidis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Raptis%2C+S">Spyros Raptis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Sung%2C+J+S">June Sig Sung</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Park%2C+H">Hyoungmin Park</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Tsiakoulis%2C+P">Pirros Tsiakoulis</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2111.09052v1-abstract-short" style="display: inline;">
            …attention-based sequence-to-sequence acoustic model and the LPCNet vocoder for waveform generation. An acoustic model architecture that adopts modules from both the <span class="search-hit mathjax">Tacotron</span> 1 and 2 models is proposed, while stability is ensured by using a recently proposed purely location-based attention mechanism, suitable for arbitrary sentence length generation. During i…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2111.09052v1-abstract-full').style.display = 'inline'; document.getElementById('2111.09052v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2111.09052v1-abstract-full" style="display: none;">
            This paper presents an end-to-end text-to-speech system with low latency on a CPU, suitable for real-time applications. The system is composed of an autoregressive attention-based sequence-to-sequence acoustic model and the LPCNet vocoder for waveform generation. An acoustic model architecture that adopts modules from both the <span class="search-hit mathjax">Tacotron</span> 1 and 2 models is proposed, while stability is ensured by using a recently proposed purely location-based attention mechanism, suitable for arbitrary sentence length generation. During inference, the decoder is unrolled and acoustic feature generation is performed in a streaming manner, allowing for a nearly constant latency which is independent from the sentence length. Experimental results show that the acoustic model can produce feature sequences with minimal latency about 31 times faster than real-time on a computer CPU and 6.5 times on a mobile CPU, enabling it to meet the conditions required for real-time applications on both devices. The full end-to-end system can generate almost natural quality speech, which is verified by listening tests.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2111.09052v1-abstract-full').style.display = 'none'; document.getElementById('2111.09052v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 17 November, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> November 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Proceedings of INTERSPEECH 2020</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2109.08710">arXiv:2109.08710</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2109.08710">pdf</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Performance">cs.PF</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            On-device neural speech synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Achanta%2C+S">Sivanand Achanta</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Antony%2C+A">Albert Antony</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Golipour%2C+L">Ladan Golipour</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+J">Jiangchuan Li</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Raitio%2C+T">Tuomo Raitio</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Rasipuram%2C+R">Ramya Rasipuram</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Rossi%2C+F">Francesco Rossi</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Shi%2C+J">Jennifer Shi</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Upadhyay%2C+J">Jaimin Upadhyay</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Winarsky%2C+D">David Winarsky</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+H">Hepeng Zhang</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2109.08710v1-abstract-short" style="display: inline;">
            Recent advances in text-to-speech (TTS) synthesis, such as <span class="search-hit mathjax">Tacotron</span> and WaveRNN, have made it possible to construct a fully neural network based TTS system, by coupling the two components together. Such a system is conceptually simple as it only takes grapheme or phoneme input, uses Mel-spectrogram as an intermediate feature, and directly generates speech sa…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2109.08710v1-abstract-full').style.display = 'inline'; document.getElementById('2109.08710v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2109.08710v1-abstract-full" style="display: none;">
            Recent advances in text-to-speech (TTS) synthesis, such as <span class="search-hit mathjax">Tacotron</span> and WaveRNN, have made it possible to construct a fully neural network based TTS system, by coupling the two components together. Such a system is conceptually simple as it only takes grapheme or phoneme input, uses Mel-spectrogram as an intermediate feature, and directly generates speech samples. The system achieves quality equal or close to natural speech. However, the high computational cost of the system and issues with robustness have limited their usage in real-world speech synthesis applications and products. In this paper, we present key modeling improvements and optimization strategies that enable deploying these models, not only on GPU servers, but also on mobile devices. The proposed system can generate high-quality 24 kHz speech at 5x faster than real time on server and 3x faster than real time on mobile devices.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2109.08710v1-abstract-full').style.display = 'none'; document.getElementById('2109.08710v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 17 September, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> September 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">7 pages 2 figures, accepted to ASRU 2021</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2108.13985">arXiv:2108.13985</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2108.13985">pdf</a>, <a href="https://arxiv.org/format/2108.13985">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Neural Sequence-to-Sequence Speech Synthesis Using a Hidden Semi-Markov Model Based Structured Attention Mechanism
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Nankaku%2C+Y">Yoshihiko Nankaku</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Sumiya%2C+K">Kenta Sumiya</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Yoshimura%2C+T">Takenori Yoshimura</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Takaki%2C+S">Shinji Takaki</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Hashimoto%2C+K">Kei Hashimoto</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Oura%2C+K">Keiichiro Oura</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Tokuda%2C+K">Keiichi Tokuda</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2108.13985v1-abstract-short" style="display: inline;">
            …synthesis using Seq2Seq models, incorporating both the benefits. Subjective evaluation experiments showed that the proposed method obtained higher mean opinion scores than <span class="search-hit mathjax">Tacotron</span> 2 on relatively small amount of training data.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2108.13985v1-abstract-full').style.display = 'inline'; document.getElementById('2108.13985v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2108.13985v1-abstract-full" style="display: none;">
            This paper proposes a novel Sequence-to-Sequence (Seq2Seq) model integrating the structure of Hidden Semi-Markov Models (HSMMs) into its attention mechanism. In speech synthesis, it has been shown that methods based on Seq2Seq models using deep neural networks can synthesize high quality speech under the appropriate conditions. However, several essential problems still have remained, i.e., requiring large amounts of training data due to an excessive degree for freedom in alignment (mapping function between two sequences), and the difficulty in handling duration due to the lack of explicit duration modeling. The proposed method defines a generative models to realize the simultaneous optimization of alignments and model parameters based on the Variational Auto-Encoder (VAE) framework, and provides monotonic alignments and explicit duration modeling based on the structure of HSMM. The proposed method can be regarded as an integration of Hidden Markov Model (HMM) based speech synthesis and deep learning based speech synthesis using Seq2Seq models, incorporating both the benefits. Subjective evaluation experiments showed that the proposed method obtained higher mean opinion scores than <span class="search-hit mathjax">Tacotron</span> 2 on relatively small amount of training data.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2108.13985v1-abstract-full').style.display = 'none'; document.getElementById('2108.13985v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 31 August, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">5 pages, 3 figures</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2108.13320">arXiv:2108.13320</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2108.13320">pdf</a>, <a href="https://arxiv.org/format/2108.13320">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Human-Computer Interaction">cs.HC</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
            
              <div class="is-inline-block" style="margin-left: 0.5rem">
                <div class="tags has-addons">
                  <span class="tag is-dark is-size-7">doi</span>
                  <span class="tag is-light is-size-7"><a class="" href="https://doi.org/10.1109/ICASSP43922.2022.9746686">10.1109/ICASSP43922.2022.9746686 <i class="fa fa-external-link" aria-hidden="true"></i></a></span>
                </div>
              </div>
            
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Neural HMMs are all you need (for high-quality attention-free TTS)
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Mehta%2C+S">Shivam Mehta</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Sz%C3%A9kely%2C+%C3%89">Éva Székely</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Beskow%2C+J">Jonas Beskow</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Henter%2C+G+E">Gustav Eje Henter</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2108.13320v6-abstract-short" style="display: inline;">
            …both worlds, by replacing attention in neural TTS with an autoregressive left-right no-skip hidden Markov model defined by a neural network. Based on this proposal, we modify <span class="search-hit mathjax">Tacotron</span> 2 to obtain an HMM-based neural TTS model with monotonic alignment, trained to maximise the full sequence likelihood without approximation. We also describe how to combine idea…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2108.13320v6-abstract-full').style.display = 'inline'; document.getElementById('2108.13320v6-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2108.13320v6-abstract-full" style="display: none;">
            Neural sequence-to-sequence TTS has achieved significantly better output quality than statistical speech synthesis using HMMs. However, neural TTS is generally not probabilistic and uses non-monotonic attention. Attention failures increase training time and can make synthesis babble incoherently. This paper describes how the old and new paradigms can be combined to obtain the advantages of both worlds, by replacing attention in neural TTS with an autoregressive left-right no-skip hidden Markov model defined by a neural network. Based on this proposal, we modify <span class="search-hit mathjax">Tacotron</span> 2 to obtain an HMM-based neural TTS model with monotonic alignment, trained to maximise the full sequence likelihood without approximation. We also describe how to combine ideas from classical and contemporary TTS for best results. The resulting example system is smaller and simpler than <span class="search-hit mathjax">Tacotron</span> 2, and learns to speak with fewer iterations and less data, whilst achieving comparable naturalness prior to the post-net. Our approach also allows easy control over speaking rate.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2108.13320v6-abstract-full').style.display = 'none'; document.getElementById('2108.13320v6-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 16 February, 2022; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 30 August, 2021;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">5 pages, 2 figures; final version for ICASSP 2022</span>
        </p>
        
    
        
          <p class="comments is-size-7">
            
    
            
              <span class="has-text-black-bis has-text-weight-semibold">MSC Class:</span>
              68T07
            
    
            
              <span class="has-text-black-bis has-text-weight-semibold">ACM Class:</span>
              I.2.7; I.2.6; G.3; H.5.5
            
          </p>
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2108.10447">arXiv:2108.10447</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2108.10447">pdf</a>, <a href="https://arxiv.org/format/2108.10447">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            One TTS Alignment To Rule Them All
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Badlani%2C+R">Rohan Badlani</a>, 
          
          <a href="/search/?searchtype=author&amp;query=%C5%81ancucki%2C+A">Adrian Łancucki</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Shih%2C+K+J">Kevin J. Shih</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Valle%2C+R">Rafael Valle</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ping%2C+W">Wei Ping</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Catanzaro%2C+B">Bryan Catanzaro</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2108.10447v1-abstract-short" style="display: inline;">
            …algorithm, and a simple and efficient static prior. In our experiments, the alignment learning framework improves all tested TTS architectures, both autoregressive (Flowtron, <span class="search-hit mathjax">Tacotron</span> 2) and non-autoregressive (FastPitch, FastSpeech 2, RAD-TTS). Specifically, it improves alignment convergence speed of existing attention-based mechanisms, simplifies the train…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2108.10447v1-abstract-full').style.display = 'inline'; document.getElementById('2108.10447v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2108.10447v1-abstract-full" style="display: none;">
            Speech-to-text alignment is a critical component of neural textto-speech (TTS) models. Autoregressive TTS models typically use an attention mechanism to learn these alignments on-line. However, these alignments tend to be brittle and often fail to generalize to long utterances and out-of-domain text, leading to missing or repeating words. Most non-autoregressive endto-end TTS models rely on durations extracted from external sources. In this paper we leverage the alignment mechanism proposed in RAD-TTS as a generic alignment learning framework, easily applicable to a variety of neural TTS models. The framework combines forward-sum algorithm, the Viterbi algorithm, and a simple and efficient static prior. In our experiments, the alignment learning framework improves all tested TTS architectures, both autoregressive (Flowtron, <span class="search-hit mathjax">Tacotron</span> 2) and non-autoregressive (FastPitch, FastSpeech 2, RAD-TTS). Specifically, it improves alignment convergence speed of existing attention-based mechanisms, simplifies the training pipeline, and makes the models more robust to errors on long utterances. Most importantly, the framework improves the perceived speech synthesis quality, as judged by human evaluators.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2108.10447v1-abstract-full').style.display = 'none'; document.getElementById('2108.10447v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 23 August, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2021.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2108.01831">arXiv:2108.01831</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2108.01831">pdf</a>, <a href="https://arxiv.org/format/2108.01831">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Information Sieve: Content Leakage Reduction in End-to-End Prosody For Expressive Speech Synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Dai%2C+X">Xudong Dai</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Gong%2C+C">Cheng Gong</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wang%2C+L">Longbiao Wang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+K">Kaili Zhang</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2108.01831v1-abstract-short" style="display: inline;">
            …model in mitigating content leakage. Listening tests indicate that the model retains its prosody transferability compared with the baseline models such as the original GST-<span class="search-hit mathjax">Tacotron</span> and ASR-guided <span class="search-hit mathjax">Tacotron</span>.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2108.01831v1-abstract-full').style.display = 'inline'; document.getElementById('2108.01831v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2108.01831v1-abstract-full" style="display: none;">
            Expressive neural text-to-speech (TTS) systems incorporate a style encoder to learn a latent embedding as the style information. However, this embedding process may encode redundant textual information. This phenomenon is called content leakage. Researchers have attempted to resolve this problem by adding an ASR or other auxiliary supervision loss functions. In this study, we propose an unsupervised method called the "information sieve" to reduce the effect of content leakage in prosody transfer. The rationale of this approach is that the style encoder can be forced to focus on style information rather than on textual information contained in the reference speech by a well-designed downsample-upsample filter, i.e., the extracted style embeddings can be downsampled at a certain interval and then upsampled by duplication. Furthermore, we used instance normalization in convolution layers to help the system learn a better latent style space. Objective metrics such as the significantly lower word error rate (WER) demonstrate the effectiveness of this model in mitigating content leakage. Listening tests indicate that the model retains its prosody transferability compared with the baseline models such as the original GST-<span class="search-hit mathjax">Tacotron</span> and ASR-guided <span class="search-hit mathjax">Tacotron</span>.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2108.01831v1-abstract-full').style.display = 'none'; document.getElementById('2108.01831v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 3 August, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Accepted By Interspeech 2021</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2107.11412">arXiv:2107.11412</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2107.11412">pdf</a>, <a href="https://arxiv.org/ps/2107.11412">ps</a>, <a href="https://arxiv.org/format/2107.11412">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Multimedia">cs.MM</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Using Deep Learning Techniques and Inferential Speech Statistics for AI Synthesised Speech Recognition
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Singh%2C+A+K">Arun Kumar Singh</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Singh%2C+P">Priyanka Singh</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Nathwani%2C+K">Karan Nathwani</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2107.11412v1-abstract-short" style="display: inline;">
            The recent developments in technology have re-warded us with amazing audio synthesis models like <span class="search-hit mathjax">TACOTRON</span> and WAVENETS. On the other side, it poses greater threats such as speech clones and deep fakes, that may go undetected. To tackle these alarming situations, there is an urgent need to propose models that can help discriminate a synthesized speech from an…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2107.11412v1-abstract-full').style.display = 'inline'; document.getElementById('2107.11412v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2107.11412v1-abstract-full" style="display: none;">
            The recent developments in technology have re-warded us with amazing audio synthesis models like <span class="search-hit mathjax">TACOTRON</span> and WAVENETS. On the other side, it poses greater threats such as speech clones and deep fakes, that may go undetected. To tackle these alarming situations, there is an urgent need to propose models that can help discriminate a synthesized speech from an actual human speech and also identify the source of such a synthesis. Here, we propose a model based on Convolutional Neural Network (CNN) and Bidirectional Recurrent Neural Network (BiRNN) that helps to achieve both the aforementioned objectives. The temporal dependencies present in AI synthesized speech are exploited using Bidirectional RNN and CNN. The model outperforms the state-of-the-art approaches by classifying the AI synthesized audio from real human speech with an error rate of 1.9% and detecting the underlying architecture with an accuracy of 97%.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2107.11412v1-abstract-full').style.display = 'none'; document.getElementById('2107.11412v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 23 July, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> July 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">13 Pages, 13 Figures, 6 Tables. arXiv admin note: substantial text overlap with arXiv:2009.01934</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2106.14213">arXiv:2106.14213</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2106.14213">pdf</a>, <a href="https://arxiv.org/format/2106.14213">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Artificial Intelligence">cs.AI</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Information Retrieval">cs.IR</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            AI based Presentation Creator With Customized Audio Content Delivery
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Mansoor%2C+M">Muvazima Mansoor</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chandar%2C+S">Srikanth Chandar</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Srinath%2C+R">Ramamoorthy Srinath</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2106.14213v1-abstract-short" style="display: inline;">
            …be the content that has to be presented. The research paper is first summarized using BERT summarization techniques and condensed into bullet points that go into the slides. <span class="search-hit mathjax">Tacotron</span> inspired architecture with Encoder, Synthesizer, and a Generative Adversarial Network (GAN) based vocoder, is used to convey the contents of the slides in the author's voice…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2106.14213v1-abstract-full').style.display = 'inline'; document.getElementById('2106.14213v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2106.14213v1-abstract-full" style="display: none;">
            In this paper, we propose an architecture to solve a novel problem statement that has stemmed more so in recent times with an increase in demand for virtual content delivery due to the COVID-19 pandemic. All educational institutions, workplaces, research centers, etc. are trying to bridge the gap of communication during these socially distanced times with the use of online content delivery. The trend now is to create presentations, and then subsequently deliver the same using various virtual meeting platforms. The time being spent in such creation of presentations and delivering is what we try to reduce and eliminate through this paper which aims to use Machine Learning (ML) algorithms and Natural Language Processing (NLP) modules to automate the process of creating a slides-based presentation from a document, and then use state-of-the-art voice cloning models to deliver the content in the desired author's voice. We consider a structured document such as a research paper to be the content that has to be presented. The research paper is first summarized using BERT summarization techniques and condensed into bullet points that go into the slides. <span class="search-hit mathjax">Tacotron</span> inspired architecture with Encoder, Synthesizer, and a Generative Adversarial Network (GAN) based vocoder, is used to convey the contents of the slides in the author's voice (or any customized voice). Almost all learning has now been shifted to online mode, and professionals are now working from the comfort of their homes. Due to the current situation, teachers and professionals have shifted to presentations to help them in imparting information. In this paper, we aim to reduce the considerable amount of time that is taken in creating a presentation by automating this process and subsequently delivering this presentation in a customized voice, using a content delivery mechanism that can clone any voice using a short audio clip.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2106.14213v1-abstract-full').style.display = 'none'; document.getElementById('2106.14213v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 27 June, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> June 2021.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2106.08352">arXiv:2106.08352</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2106.08352">pdf</a>, <a href="https://arxiv.org/format/2106.08352">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Ctrl-P: Temporal Control of Prosodic Variation for Speech Synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Mohan%2C+D+S+R">Devang S Ram Mohan</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Hu%2C+V">Vivian Hu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Teh%2C+T+H">Tian Huey Teh</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Torresquintero%2C+A">Alexandra Torresquintero</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wallis%2C+C+G+R">Christopher G. R. Wallis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Staib%2C+M">Marlene Staib</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Foglianti%2C+L">Lorenzo Foglianti</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Gao%2C+J">Jiameng Gao</a>, 
          
          <a href="/search/?searchtype=author&amp;query=King%2C+S">Simon King</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2106.08352v1-abstract-short" style="display: inline;">
            …temporally-precise, and disentangled control. When automatically predicting the acoustic features from text, it generates speech that is more natural than that from a <span class="search-hit mathjax">Tacotron</span> 2 model with reference encoder. Subsequent human-in-the-loop modification of the predicted acoustic features can significantly further increase naturalness.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2106.08352v1-abstract-full').style.display = 'inline'; document.getElementById('2106.08352v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2106.08352v1-abstract-full" style="display: none;">
            Text does not fully specify the spoken form, so text-to-speech models must be able to learn from speech data that vary in ways not explained by the corresponding text. One way to reduce the amount of unexplained variation in training data is to provide acoustic information as an additional learning signal. When generating speech, modifying this acoustic information enables multiple distinct renditions of a text to be produced.
     
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2106.08352v1-abstract-full').style.display = 'none'; document.getElementById('2106.08352v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 15 June, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> June 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">To be published in Interspeech 2021. 5 pages, 4 figures</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2105.01891">arXiv:2105.01891</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2105.01891">pdf</a>, <a href="https://arxiv.org/format/2105.01891">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Human-Computer Interaction">cs.HC</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
            </div>
          
            
              <div class="is-inline-block" style="margin-left: 0.5rem">
                <div class="tags has-addons">
                  <span class="tag is-dark is-size-7">doi</span>
                  <span class="tag is-light is-size-7"><a class="" href="https://doi.org/10.21437/Interspeech.2021-1538">10.21437/Interspeech.2021-1538 <i class="fa fa-external-link" aria-hidden="true"></i></a></span>
                </div>
              </div>
            
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Exploring emotional prototypes in a high dimensional TTS latent space
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=van+Rijn%2C+P">Pol van Rijn</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Mertes%2C+S">Silvan Mertes</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Schiller%2C+D">Dominik Schiller</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Harrison%2C+P+M+C">Peter M. C. Harrison</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Larrouy-Maestri%2C+P">Pauline Larrouy-Maestri</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Andr%C3%A9%2C+E">Elisabeth André</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Jacoby%2C+N">Nori Jacoby</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2105.01891v1-abstract-short" style="display: inline;">
            …of speakers' emotional states. Here we use the recent psychological paradigm 'Gibbs Sampling with People' to search the prosodic latent space in a trained GST <span class="search-hit mathjax">Tacotron</span> model to explore prototypes of emotional prosody. Participants are recruited online and collectively manipulate the latent space of the generative speech model in a sequentially ad…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2105.01891v1-abstract-full').style.display = 'inline'; document.getElementById('2105.01891v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2105.01891v1-abstract-full" style="display: none;">
            Recent TTS systems are able to generate prosodically varied and realistic speech. However, it is unclear how this prosodic variation contributes to the perception of speakers' emotional states. Here we use the recent psychological paradigm 'Gibbs Sampling with People' to search the prosodic latent space in a trained GST <span class="search-hit mathjax">Tacotron</span> model to explore prototypes of emotional prosody. Participants are recruited online and collectively manipulate the latent space of the generative speech model in a sequentially adaptive way so that the stimulus presented to one group of participants is determined by the response of the previous groups. We demonstrate that (1) particular regions of the model's latent space are reliably associated with particular emotions, (2) the resulting emotional prototypes are well-recognized by a separate group of human raters, and (3) these emotional prototypes can be effectively transferred to new sentences. Collectively, these experiments demonstrate a novel approach to the understanding of emotional speech by providing a tool to explore the relation between the latent space of generative models and human semantics.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2105.01891v1-abstract-full').style.display = 'none'; document.getElementById('2105.01891v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 5 May, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> May 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Submitted to INTERSPEECH'21</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2104.12292">arXiv:2104.12292</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2104.12292">pdf</a>, <a href="https://arxiv.org/format/2104.12292">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Text-to-Speech Synthesis Techniques for MIDI-to-Audio Synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Cooper%2C+E">Erica Cooper</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wang%2C+X">Xin Wang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Yamagishi%2C+J">Junichi Yamagishi</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2104.12292v6-abstract-short" style="display: inline;">
            …share some similarities. In this study, we investigate how text-to-speech synthesis techniques can be used for piano MIDI-to-audio synthesis tasks. Our investigation includes <span class="search-hit mathjax">Tacotron</span> and neural source-filter waveform models as the basic components, with which we build MIDI-to-audio synthesis systems in similar ways to TTS frameworks. We also include referen…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2104.12292v6-abstract-full').style.display = 'inline'; document.getElementById('2104.12292v6-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2104.12292v6-abstract-full" style="display: none;">
            Speech synthesis and music audio generation from symbolic input differ in many aspects but share some similarities. In this study, we investigate how text-to-speech synthesis techniques can be used for piano MIDI-to-audio synthesis tasks. Our investigation includes <span class="search-hit mathjax">Tacotron</span> and neural source-filter waveform models as the basic components, with which we build MIDI-to-audio synthesis systems in similar ways to TTS frameworks. We also include reference systems using conventional sound modeling techniques such as sample-based and physical-modeling-based methods. The subjective experimental results demonstrate that the investigated TTS components can be applied to piano MIDI-to-audio synthesis with minor modifications. The results also reveal the performance bottleneck -- while the waveform model can synthesize high quality piano sound given natural acoustic features, the conversion from MIDI to acoustic features is challenging. The full MIDI-to-audio synthesis system is still inferior to the sample-based or physical-modeling-based approaches, but we encourage TTS researchers to test their TTS models for this new task and improve the performance.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2104.12292v6-abstract-full').style.display = 'none'; document.getElementById('2104.12292v6-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 24 February, 2022; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 25 April, 2021;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> April 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">In the proceedings of ISCA Speech Synthesis Workshop 2021</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2104.04050">arXiv:2104.04050</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2104.04050">pdf</a>, <a href="https://arxiv.org/format/2104.04050">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Flavored <span class="search-hit mathjax">Tacotron</span>: Conditional Learning for Prosodic-linguistic Features
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Elyasi%2C+M">Mahsa Elyasi</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Bharaj%2C+G">Gaurav Bharaj</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2104.04050v1-abstract-short" style="display: inline;">
            Neural sequence-to-sequence text-to-speech synthesis (TTS), such as <span class="search-hit mathjax">Tacotron</span>-2, transforms text into high-quality speech. However, generating speech with natural prosody still remains a challenge. Yasuda et. al. show that unlike natural speech,…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2104.04050v1-abstract-full').style.display = 'inline'; document.getElementById('2104.04050v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2104.04050v1-abstract-full" style="display: none;">
            Neural sequence-to-sequence text-to-speech synthesis (TTS), such as <span class="search-hit mathjax">Tacotron</span>-2, transforms text into high-quality speech. However, generating speech with natural prosody still remains a challenge. Yasuda et. al. show that unlike natural speech, <span class="search-hit mathjax">Tacotron</span>-2's encoder doesn't fully represent prosodic features (e.g. syllable stress in English) from characters, and result in flat fundamental frequency variations.
      In this work, we propose a novel carefully designed strategy for conditioning <span class="search-hit mathjax">Tacotron</span>-2 on two fundamental prosodic features in English -- stress syllable and pitch accent, that help achieve more natural prosody. To this end, we use of a classifier to learn these features in an end-to-end fashion, and apply feature conditioning at three parts of <span class="search-hit mathjax">Tacotron</span>-2's Text-To-Mel Spectrogram: pre-encoder, post-encoder, and intra-decoder. Further, we show that jointly conditioned features at pre-encoder and intra-decoder stages result in prosodically natural synthesized speech (vs. <span class="search-hit mathjax">Tacotron</span>-2), and allows the model to produce speech with more accurate pitch accent and stress patterns.
      Quantitative evaluations show that our formulation achieves higher fundamental frequency contour correlation, and lower Mel Cepstral Distortion measure between synthesized and natural speech. And subjective evaluation shows that the proposed method's Mean Opinion Score of 4.14 fairs higher than baseline <span class="search-hit mathjax">Tacotron</span>-2, 3.91, when compared against natural speech (LJSpeech corpus), 4.28.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2104.04050v1-abstract-full').style.display = 'none'; document.getElementById('2104.04050v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 8 April, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> April 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">5</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2103.14574">arXiv:2103.14574</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2103.14574">pdf</a>, <a href="https://arxiv.org/format/2103.14574">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Parallel <span class="search-hit mathjax">Tacotron</span> 2: A Non-Autoregressive Neural TTS Model with Differentiable Duration Modeling
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Elias%2C+I">Isaac Elias</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zen%2C+H">Heiga Zen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Shen%2C+J">Jonathan Shen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+Y">Yu Zhang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Jia%2C+Y">Ye Jia</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Skerry-Ryan%2C+R">RJ Skerry-Ryan</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wu%2C+Y">Yonghui Wu</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2103.14574v7-abstract-short" style="display: inline;">
            This paper introduces Parallel <span class="search-hit mathjax">Tacotron</span> 2, a non-autoregressive neural text-to-speech model with a fully differentiable duration model which does not require supervised duration signals. The duration model is based on a novel attention mechanism and an iterative reconstruction loss based on Soft Dynamic Time Warping, this model can learn token-frame alignmen…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2103.14574v7-abstract-full').style.display = 'inline'; document.getElementById('2103.14574v7-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2103.14574v7-abstract-full" style="display: none;">
            This paper introduces Parallel <span class="search-hit mathjax">Tacotron</span> 2, a non-autoregressive neural text-to-speech model with a fully differentiable duration model which does not require supervised duration signals. The duration model is based on a novel attention mechanism and an iterative reconstruction loss based on Soft Dynamic Time Warping, this model can learn token-frame alignments as well as token durations automatically. Experimental results show that Parallel <span class="search-hit mathjax">Tacotron</span> 2 outperforms baselines in subjective naturalness in several diverse multi speaker evaluations. Its duration control capability is also demonstrated.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2103.14574v7-abstract-full').style.display = 'none'; document.getElementById('2103.14574v7-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 29 August, 2021; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 26 March, 2021;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> March 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Submitted to INTERSPEECH 2021</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2102.06431">arXiv:2102.06431</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2102.06431">pdf</a>, <a href="https://arxiv.org/format/2102.06431">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            VARA-TTS: Non-Autoregressive Text-to-Speech Synthesis based on Very Deep VAE with Residual Attention
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Liu%2C+P">Peng Liu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Cao%2C+Y">Yuewen Cao</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Liu%2C+S">Songxiang Liu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Hu%2C+N">Na Hu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+G">Guangzhi Li</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Weng%2C+C">Chao Weng</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Su%2C+D">Dan Su</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2102.06431v1-abstract-short" style="display: inline;">
            …layer as input, to determine number of acoustic frames at inference. Experimental results show that VARA-TTS achieves slightly inferior speech quality to an AR counterpart <span class="search-hit mathjax">Tacotron</span> 2 but an order-of-magnitude speed-up at inference; and outperforms an analogous non-AR model, BVAE-TTS, in terms of speech quality.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2102.06431v1-abstract-full').style.display = 'inline'; document.getElementById('2102.06431v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2102.06431v1-abstract-full" style="display: none;">
            This paper proposes VARA-TTS, a non-autoregressive (non-AR) text-to-speech (TTS) model using a very deep Variational Autoencoder (VDVAE) with Residual Attention mechanism, which refines the textual-to-acoustic alignment layer-wisely. Hierarchical latent variables with different temporal resolutions from the VDVAE are used as queries for residual attention module. By leveraging the coarse global alignment from previous attention layer as an extra input, the following attention layer can produce a refined version of alignment. This amortizes the burden of learning the textual-to-acoustic alignment among multiple attention layers and outperforms the use of only a single attention layer in robustness. An utterance-level speaking speed factor is computed by a jointly-trained speaking speed predictor, which takes the mean-pooled latent variables of the coarsest layer as input, to determine number of acoustic frames at inference. Experimental results show that VARA-TTS achieves slightly inferior speech quality to an AR counterpart <span class="search-hit mathjax">Tacotron</span> 2 but an order-of-magnitude speed-up at inference; and outperforms an analogous non-AR model, BVAE-TTS, in terms of speech quality.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2102.06431v1-abstract-full').style.display = 'none'; document.getElementById('2102.06431v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 12 February, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> February 2021.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2101.05313">arXiv:2101.05313</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2101.05313">pdf</a>, <a href="https://arxiv.org/format/2101.05313">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Whispered and Lombard Neural Speech Synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Hu%2C+Q">Qiong Hu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Bleisch%2C+T">Tobias Bleisch</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Petkov%2C+P">Petko Petkov</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Raitio%2C+T">Tuomo Raitio</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Marchi%2C+E">Erik Marchi</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Lakshminarasimhan%2C+V">Varun Lakshminarasimhan</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2101.05313v1-abstract-short" style="display: inline;">
            …and no Lombard and whisper voice is used for pre-training this system, the SV model can be used as a style encoder for generating different style embeddings as input for the <span class="search-hit mathjax">Tacotron</span> system. We also show that the resulting synthetic Lombard speech has a significant positive impact on intelligibility gain.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2101.05313v1-abstract-full').style.display = 'inline'; document.getElementById('2101.05313v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2101.05313v1-abstract-full" style="display: none;">
            It is desirable for a text-to-speech system to take into account the environment where synthetic speech is presented, and provide appropriate context-dependent output to the user. In this paper, we present and compare various approaches for generating different speaking styles, namely, normal, Lombard, and whisper speech, using only limited data. The following systems are proposed and assessed: 1) Pre-training and fine-tuning a model for each style. 2) Lombard and whisper speech conversion through a signal processing based approach. 3) Multi-style generation using a single model based on a speaker verification model. Our mean opinion score and AB preference listening tests show that 1) we can generate high quality speech through the pre-training/fine-tuning approach for all speaking styles. 2) Although our speaker verification (SV) model is not explicitly trained to discriminate different speaking styles, and no Lombard and whisper voice is used for pre-training this system, the SV model can be used as a style encoder for generating different style embeddings as input for the <span class="search-hit mathjax">Tacotron</span> system. We also show that the resulting synthetic Lombard speech has a significant positive impact on intelligibility gain.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2101.05313v1-abstract-full').style.display = 'none'; document.getElementById('2101.05313v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 13 January, 2021; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> January 2021.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">To appear in SLT 2021</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2012.09703">arXiv:2012.09703</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2012.09703">pdf</a>, <a href="https://arxiv.org/format/2012.09703">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Parallel WaveNet conditioned on VAE latent vectors
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Rohnke%2C+J">Jonas Rohnke</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Merritt%2C+T">Tom Merritt</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Lorenzo-Trueba%2C+J">Jaime Lorenzo-Trueba</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Gabrys%2C+A">Adam Gabrys</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Aggarwal%2C+V">Vatsal Aggarwal</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Moinet%2C+A">Alexis Moinet</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Barra-Chicote%2C+R">Roberto Barra-Chicote</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2012.09703v1-abstract-short" style="display: inline;">
            …vector to improve the signal quality of a Parallel WaveNet neural vocoder. We condition the neural vocoder with the latent vector from a pre-trained VAE component of a <span class="search-hit mathjax">Tacotron</span> 2-style sequence-to-sequence model. With this, we are able to significantly improve the quality of vocoded speech.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2012.09703v1-abstract-full').style.display = 'inline'; document.getElementById('2012.09703v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2012.09703v1-abstract-full" style="display: none;">
            Recently the state-of-the-art text-to-speech synthesis systems have shifted to a two-model approach: a sequence-to-sequence model to predict a representation of speech (typically mel-spectrograms), followed by a 'neural vocoder' model which produces the time-domain speech waveform from this intermediate speech representation. This approach is capable of synthesizing speech that is confusable with natural speech recordings. However, the inference speed of neural vocoder approaches represents a major obstacle for deploying this technology for commercial applications. Parallel WaveNet is one approach which has been developed to address this issue, trading off some synthesis quality for significantly faster inference speed. In this paper we investigate the use of a sentence-level conditioning vector to improve the signal quality of a Parallel WaveNet neural vocoder. We condition the neural vocoder with the latent vector from a pre-trained VAE component of a <span class="search-hit mathjax">Tacotron</span> 2-style sequence-to-sequence model. With this, we are able to significantly improve the quality of vocoded speech.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2012.09703v1-abstract-full').style.display = 'none'; document.getElementById('2012.09703v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 17 December, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> December 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2012.03763">arXiv:2012.03763</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2012.03763">pdf</a>, <a href="https://arxiv.org/format/2012.03763">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Using previous acoustic context to improve Text-to-Speech synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Oplustil-Gallegos%2C+P">Pilar Oplustil-Gallegos</a>, 
          
          <a href="/search/?searchtype=author&amp;query=King%2C+S">Simon King</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2012.03763v1-abstract-short" style="display: inline;">
            …we leverage the sequential nature of the data using an acoustic context encoder that produces an embedding of the previous utterance audio. This is input to the decoder in a <span class="search-hit mathjax">Tacotron</span> 2 model. The embedding is also used for a secondary task, providing additional supervision. We compare two secondary tasks: predicting the ordering of utterance pairs, and pred…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2012.03763v1-abstract-full').style.display = 'inline'; document.getElementById('2012.03763v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2012.03763v1-abstract-full" style="display: none;">
            Many speech synthesis datasets, especially those derived from audiobooks, naturally comprise sequences of utterances. Nevertheless, such data are commonly treated as individual, unordered utterances both when training a model and at inference time. This discards important prosodic phenomena above the utterance level. In this paper, we leverage the sequential nature of the data using an acoustic context encoder that produces an embedding of the previous utterance audio. This is input to the decoder in a <span class="search-hit mathjax">Tacotron</span> 2 model. The embedding is also used for a secondary task, providing additional supervision. We compare two secondary tasks: predicting the ordering of utterance pairs, and predicting the embedding of the current utterance audio. Results show that the relation between consecutive utterances is informative: our proposed model significantly improves naturalness over a <span class="search-hit mathjax">Tacotron</span> 2 baseline.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2012.03763v1-abstract-full').style.display = 'none'; document.getElementById('2012.03763v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 7 December, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> December 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2012.03500">arXiv:2012.03500</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2012.03500">pdf</a>, <a href="https://arxiv.org/format/2012.03500">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            EfficientTTS: An Efficient and High-Quality Text-to-Speech Architecture
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Miao%2C+C">Chenfeng Miao</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Liang%2C+S">Shuang Liang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Liu%2C+Z">Zhencheng Liu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chen%2C+M">Minchuan Chen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ma%2C+J">Jun Ma</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wang%2C+S">Shaojun Wang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Xiao%2C+J">Jing Xiao</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2012.03500v1-abstract-short" style="display: inline;">
            …including both text-to-melspectrogram and text-to-waveform networks. We experimentally show that the proposed models significantly outperform counterpart models such as <span class="search-hit mathjax">Tacotron</span> 2 and Glow-TTS in terms of speech quality, training efficiency and synthesis speed, while still producing the speeches of strong robustness and great diversity. In addition, we demo…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2012.03500v1-abstract-full').style.display = 'inline'; document.getElementById('2012.03500v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2012.03500v1-abstract-full" style="display: none;">
            In this work, we address the Text-to-Speech (TTS) task by proposing a non-autoregressive architecture called EfficientTTS. Unlike the dominant non-autoregressive TTS models, which are trained with the need of external aligners, EfficientTTS optimizes all its parameters with a stable, end-to-end training procedure, while allowing for synthesizing high quality speech in a fast and efficient manner. EfficientTTS is motivated by a new monotonic alignment modeling approach (also introduced in this work), which specifies monotonic constraints to the sequence alignment with almost no increase of computation. By combining EfficientTTS with different feed-forward network structures, we develop a family of TTS models, including both text-to-melspectrogram and text-to-waveform networks. We experimentally show that the proposed models significantly outperform counterpart models such as <span class="search-hit mathjax">Tacotron</span> 2 and Glow-TTS in terms of speech quality, training efficiency and synthesis speed, while still producing the speeches of strong robustness and great diversity. In addition, we demonstrate that proposed approach can be easily extended to autoregressive models such as <span class="search-hit mathjax">Tacotron</span> 2.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2012.03500v1-abstract-full').style.display = 'none'; document.getElementById('2012.03500v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 7 December, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> December 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">15 pages, 9 figures</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2011.08679">arXiv:2011.08679</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2011.08679">pdf</a>, <a href="https://arxiv.org/format/2011.08679">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Controllable Emotion Transfer For End-to-End Speech Synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+T">Tao Li</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Yang%2C+S">Shan Yang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Xue%2C+L">Liumeng Xue</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Xie%2C+L">Lei Xie</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2011.08679v1-abstract-short" style="display: inline;">
            …category confusions. Moreover, it is hard to select an appropriate reference to deliver desired emotion strength. To solve these problems, we propose a novel approach based on <span class="search-hit mathjax">Tacotron</span>. First, we plug two emotion classifiers -- one after the reference encoder, one after the decoder output -- to enhance the emotion-discriminative ability of the emotion embedd…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2011.08679v1-abstract-full').style.display = 'inline'; document.getElementById('2011.08679v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2011.08679v1-abstract-full" style="display: none;">
            Emotion embedding space learned from references is a straightforward approach for emotion transfer in encoder-decoder structured emotional text to speech (TTS) systems. However, the transferred emotion in the synthetic speech is not accurate and expressive enough with emotion category confusions. Moreover, it is hard to select an appropriate reference to deliver desired emotion strength. To solve these problems, we propose a novel approach based on <span class="search-hit mathjax">Tacotron</span>. First, we plug two emotion classifiers -- one after the reference encoder, one after the decoder output -- to enhance the emotion-discriminative ability of the emotion embedding and the predicted mel-spectrum. Second, we adopt style loss to measure the difference between the generated and reference mel-spectrum. The emotion strength in the synthetic speech can be controlled by adjusting the value of the emotion embedding as the emotion embedding can be viewed as the feature map of the mel-spectrum. Experiments on emotion transfer and strength control have shown that the synthetic speech of the proposed method is more accurate and expressive with less emotion category confusions and the control of emotion strength is more salient to listeners.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2011.08679v1-abstract-full').style.display = 'none'; document.getElementById('2011.08679v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 17 November, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> November 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2011.08480">arXiv:2011.08480</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2011.08480">pdf</a>, <a href="https://arxiv.org/format/2011.08480">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            s-Transformer: Segment-Transformer for Robust Neural Speech Synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Wang%2C+X">Xi Wang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ming%2C+H">Huaiping Ming</a>, 
          
          <a href="/search/?searchtype=author&amp;query=He%2C+L">Lei He</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Soong%2C+F+K">Frank K. Soong</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2011.08480v1-abstract-short" style="display: inline;">
            Neural end-to-end text-to-speech (TTS) , which adopts either a recurrent model, e.g. <span class="search-hit mathjax">Tacotron</span>, or an attention one, e.g. Transformer, to characterize a speech utterance, has achieved significant improvement of speech synthesis. However, it is still very challenging to deal with different sentence lengths, particularly, for long sentences where sequence model…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2011.08480v1-abstract-full').style.display = 'inline'; document.getElementById('2011.08480v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2011.08480v1-abstract-full" style="display: none;">
            Neural end-to-end text-to-speech (TTS) , which adopts either a recurrent model, e.g. <span class="search-hit mathjax">Tacotron</span>, or an attention one, e.g. Transformer, to characterize a speech utterance, has achieved significant improvement of speech synthesis. However, it is still very challenging to deal with different sentence lengths, particularly, for long sentences where sequence model has limitation of the effective context length. We propose a novel segment-Transformer (s-Transformer), which models speech at segment level where recurrence is reused via cached memories for both the encoder and decoder. Long-range contexts can be captured by the extended memory, meanwhile, the encoder-decoder attention on segment which is much easier to handle. In addition, we employ a modified relative positional self attention to generalize sequence length beyond a period possibly unseen in the training data. By comparing the proposed s-Transformer with the standard Transformer, on short sentences, both achieve the same MOS scores of 4.29, which is very close to 4.32 by the recordings; similar scores of 4.22 vs 4.2 on long sentences, and significantly better for extra-long sentences with a gain of 0.2 in MOS. Since the cached memory is updated with time, the s-Transformer generates rather natural and coherent speech for a long period of time.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2011.08480v1-abstract-full').style.display = 'none'; document.getElementById('2011.08480v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 17 November, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> November 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">5 pages, 5 figures</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2011.06392">arXiv:2011.06392</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2011.06392">pdf</a>, <a href="https://arxiv.org/format/2011.06392">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Using IPA-Based <span class="search-hit mathjax">Tacotron</span> for Data Efficient Cross-Lingual Speaker Adaptation and Pronunciation Enhancement
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Hemati%2C+H">Hamed Hemati</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Borth%2C+D">Damian Borth</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2011.06392v2-abstract-short" style="display: inline;">
            …However, fine-tuning them for new speakers or languages is not straightforward in a low-resource setup. In this paper, we show that by applying minor modifications to a <span class="search-hit mathjax">Tacotron</span> model, one can transfer an existing TTS model for new speakers from the same or a different language using only 20 minutes of data. For this purpose, we first introduce a base multi…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2011.06392v2-abstract-full').style.display = 'inline'; document.getElementById('2011.06392v2-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2011.06392v2-abstract-full" style="display: none;">
            Recent neural Text-to-Speech (TTS) models have been shown to perform very well when enough data is available. However, fine-tuning them for new speakers or languages is not straightforward in a low-resource setup. In this paper, we show that by applying minor modifications to a <span class="search-hit mathjax">Tacotron</span> model, one can transfer an existing TTS model for new speakers from the same or a different language using only 20 minutes of data. For this purpose, we first introduce a base multi-lingual <span class="search-hit mathjax">Tacotron</span> with language-agnostic input, then demonstrate how transfer learning is done for different scenarios of speaker adaptation without exploiting any pre-trained speaker encoder or code-switching technique. We evaluate the transferred model in both subjective and objective ways.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2011.06392v2-abstract-full').style.display = 'none'; document.getElementById('2011.06392v2-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 31 March, 2022; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 12 November, 2020;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> November 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Preprint</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2011.03568">arXiv:2011.03568</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2011.03568">pdf</a>, <a href="https://arxiv.org/format/2011.03568">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Wave-<span class="search-hit mathjax">Tacotron</span>: Spectrogram-free end-to-end text-to-speech synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Weiss%2C+R+J">Ron J. Weiss</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Skerry-Ryan%2C+R">RJ Skerry-Ryan</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Battenberg%2C+E">Eric Battenberg</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Mariooryad%2C+S">Soroosh Mariooryad</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Kingma%2C+D+P">Diederik P. Kingma</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2011.03568v2-abstract-short" style="display: inline;">
            We describe a sequence-to-sequence neural network which directly generates speech waveforms from text inputs. The architecture extends the <span class="search-hit mathjax">Tacotron</span> model by incorporating a normalizing flow into the autoregressive decoder loop. Output waveforms are modeled as a sequence of non-overlapping fixed-length blocks, each one containing hundreds of samples. The inte…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2011.03568v2-abstract-full').style.display = 'inline'; document.getElementById('2011.03568v2-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2011.03568v2-abstract-full" style="display: none;">
            We describe a sequence-to-sequence neural network which directly generates speech waveforms from text inputs. The architecture extends the <span class="search-hit mathjax">Tacotron</span> model by incorporating a normalizing flow into the autoregressive decoder loop. Output waveforms are modeled as a sequence of non-overlapping fixed-length blocks, each one containing hundreds of samples. The interdependencies of waveform samples within each block are modeled using the normalizing flow, enabling parallel training and synthesis. Longer-term dependencies are handled autoregressively by conditioning each flow on preceding blocks.This model can be optimized directly with maximum likelihood, with-out using intermediate, hand-designed features nor additional loss terms. Contemporary state-of-the-art text-to-speech (TTS) systems use a cascade of separately learned models: one (such as <span class="search-hit mathjax">Tacotron</span>) which generates intermediate features (such as spectrograms) from text, followed by a vocoder (such as WaveRNN) which generates waveform samples from the intermediate features. The proposed system, in contrast, does not use a fixed intermediate representation, and learns all parameters end-to-end. Experiments show that the proposed model generates speech with quality approaching a state-of-the-art neural TTS system, with significantly improved generation speed.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2011.03568v2-abstract-full').style.display = 'none'; document.getElementById('2011.03568v2-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 5 February, 2021; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 6 November, 2020;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> November 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">6 pages including supplement, 3 figures. accepted to ICASSP 2021</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2011.00935">arXiv:2011.00935</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2011.00935">pdf</a>, <a href="https://arxiv.org/format/2011.00935">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            FeatherTTS: Robust and Efficient attention based Neural TTS
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Tian%2C+Q">Qiao Tian</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+Z">Zewang Zhang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Liu%2C+C">Chao Liu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Lu%2C+H">Heng Lu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chen%2C+L">Linghui Chen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wei%2C+B">Bin Wei</a>, 
          
          <a href="/search/?searchtype=author&amp;query=He%2C+P">Pujiang He</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Liu%2C+S">Shan Liu</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2011.00935v1-abstract-short" style="display: inline;">
          
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2011.00935v1-abstract-full').style.display = 'inline'; document.getElementById('2011.00935v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2011.00935v1-abstract-full" style="display: none;">
        </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 2 November, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> November 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2010.15317">arXiv:2010.15317</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2010.15317">pdf</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            The IQIYI System for Voice Conversion Challenge 2020
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Gan%2C+W">Wendong Gan</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chen%2C+H">Haitao Chen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Yan%2C+Y">Yin Yan</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+J">Jianwei Li</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wen%2C+B">Bolong Wen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Xu%2C+X">Xueping Xu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+H">Hai Li</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2010.15317v1-abstract-short" style="display: inline;">
            …ASR acoustic model calculates the BN feature, which represents the content-related information in the speech. Then the Mel feature is calculated through an improved prosody <span class="search-hit mathjax">tacotron</span> model. Finally, the Mel spectrum is converted to wav through an improved LPCNet. The evaluation results show that this system can achieve better voice conversion effects. In the…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.15317v1-abstract-full').style.display = 'inline'; document.getElementById('2010.15317v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2010.15317v1-abstract-full" style="display: none;">
            This paper presents the IQIYI voice conversion system (T24) for Voice Conversion 2020. In the competition, each target speaker has 70 sentences. We have built an end-to-end voice conversion system based on PPG. First, the ASR acoustic model calculates the BN feature, which represents the content-related information in the speech. Then the Mel feature is calculated through an improved prosody <span class="search-hit mathjax">tacotron</span> model. Finally, the Mel spectrum is converted to wav through an improved LPCNet. The evaluation results show that this system can achieve better voice conversion effects. In the case of using 16k rather than 24k sampling rate audio, the conversion result is relatively good in naturalness and similarity. Among them, our best results are in the similarity evaluation of the Task 2, the 2nd in the ASV-based objective evaluation and the 5th in the subjective evaluation.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.15317v1-abstract-full').style.display = 'none'; document.getElementById('2010.15317v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 28 October, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> October 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2010.15311">arXiv:2010.15311</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2010.15311">pdf</a>, <a href="https://arxiv.org/format/2010.15311">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            DeviceTTS: A Small-Footprint, Fast, Stable Network for On-Device Text-to-Speech
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Huang%2C+Z">Zhiying Huang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+H">Hao Li</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Lei%2C+M">Ming Lei</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2010.15311v2-abstract-short" style="display: inline;">
            …proposed, named as DeviceTTS. DeviceTTS makes use of a duration predictor as a bridge between encoder and decoder so as to avoid the problem of words skipping and repeating in <span class="search-hit mathjax">Tacotron</span>. As we all know, model size is a key factor for on-device TTS. For DeviceTTS, Deep Feedforward Sequential Memory Network (DFSMN) is used as the basic component. Moreover, to s…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.15311v2-abstract-full').style.display = 'inline'; document.getElementById('2010.15311v2-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2010.15311v2-abstract-full" style="display: none;">
            With the number of smart devices increasing, the demand for on-device text-to-speech (TTS) increases rapidly. In recent years, many prominent End-to-End TTS methods have been proposed, and have greatly improved the quality of synthesized speech. However, to ensure the qualified speech, most TTS systems depend on large and complex neural network models, and it's hard to deploy these TTS systems on-device. In this paper, a small-footprint, fast, stable network for on-device TTS is proposed, named as DeviceTTS. DeviceTTS makes use of a duration predictor as a bridge between encoder and decoder so as to avoid the problem of words skipping and repeating in <span class="search-hit mathjax">Tacotron</span>. As we all know, model size is a key factor for on-device TTS. For DeviceTTS, Deep Feedforward Sequential Memory Network (DFSMN) is used as the basic component. Moreover, to speed up inference, mix-resolution decoder is proposed for balance the inference speed and speech quality. Experiences are done with WORLD and LPCNet vocoder. Finally, with only 1.4 million model parameters and 0.099 GFLOPS, DeviceTTS achieves comparable performance with <span class="search-hit mathjax">Tacotron</span> and FastSpeech. As far as we know, the DeviceTTS can meet the needs of most of the devices in practical application.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.15311v2-abstract-full').style.display = 'none'; document.getElementById('2010.15311v2-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 14 January, 2021; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 28 October, 2020;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> October 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">5 pages, 1 figure, Submitted to ICASSP2021</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2010.11567">arXiv:2010.11567</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2010.11567">pdf</a>, <a href="https://arxiv.org/format/2010.11567">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            AISHELL-3: A Multi-speaker Mandarin TTS Corpus and the Baselines
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Shi%2C+Y">Yao Shi</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Bu%2C+H">Hui Bu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Xu%2C+X">Xin Xu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+S">Shaoji Zhang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+M">Ming Li</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2010.11567v2-abstract-short" style="display: inline;">
            …with the recordings. We present a baseline system that uses AISHELL-3 for multi-speaker Madarin speech synthesis. The multi-speaker speech synthesis system is an extension on <span class="search-hit mathjax">Tacotron</span>-2 where a speaker verification model and a corresponding loss regarding voice similarity are incorporated as the feedback constraint. We aim to use the presented corpus to buil…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.11567v2-abstract-full').style.display = 'inline'; document.getElementById('2010.11567v2-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2010.11567v2-abstract-full" style="display: none;">
         
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.11567v2-abstract-full').style.display = 'none'; document.getElementById('2010.11567v2-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 22 April, 2021; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 22 October, 2020;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> October 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2010.11439">arXiv:2010.11439</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2010.11439">pdf</a>, <a href="https://arxiv.org/format/2010.11439">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Parallel <span class="search-hit mathjax">Tacotron</span>: Non-Autoregressive and Controllable TTS
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Elias%2C+I">Isaac Elias</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zen%2C+H">Heiga Zen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Shen%2C+J">Jonathan Shen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+Y">Yu Zhang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Jia%2C+Y">Ye Jia</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Weiss%2C+R">Ron Weiss</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wu%2C+Y">Yonghui Wu</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2010.11439v1-abstract-short" style="display: inline;">
            …This paper proposes a non-autoregressive neural text-to-speech model augmented with a variational autoencoder-based residual encoder. This model, called \emph{Parallel <span class="search-hit mathjax">Tacotron</span>}, is highly parallelizable during both training and inference, allowing efficient synthesis on modern parallel hardware. The use of the variational autoencoder relaxes the one-to-man…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.11439v1-abstract-full').style.display = 'inline'; document.getElementById('2010.11439v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2010.11439v1-abstract-full" style="display: none;">
            Although neural end-to-end text-to-speech models can synthesize highly natural speech, there is still room for improvements to its efficiency and naturalness. This paper proposes a non-autoregressive neural text-to-speech model augmented with a variational autoencoder-based residual encoder. This model, called \emph{Parallel <span class="search-hit mathjax">Tacotron</span>}, is highly parallelizable during both training and inference, allowing efficient synthesis on modern parallel hardware. The use of the variational autoencoder relaxes the one-to-many mapping nature of the text-to-speech problem and improves naturalness. To further improve the naturalness, we use lightweight convolutions, which can efficiently capture local contexts, and introduce an iterative spectrogram loss inspired by iterative refinement. Experimental results show that Parallel <span class="search-hit mathjax">Tacotron</span> matches a strong autoregressive baseline in subjective evaluations with significantly decreased inference time.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.11439v1-abstract-full').style.display = 'none'; document.getElementById('2010.11439v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 22 October, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> October 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2010.11221">arXiv:2010.11221</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2010.11221">pdf</a>, <a href="https://arxiv.org/format/2010.11221">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Learning Speaker Embedding from Text-to-Speech
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Cho%2C+J">Jaejin Cho</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zelasko%2C+P">Piotr Zelasko</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Villalba%2C+J">Jesus Villalba</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Watanabe%2C+S">Shinji Watanabe</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Dehak%2C+N">Najim Dehak</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2010.11221v1-abstract-short" style="display: inline;">
            …In this work, we investigate the effectiveness of the TTS reconstruction objective to improve representation learning for speaker verification. We jointly trained end-to-end <span class="search-hit mathjax">Tacotron</span> 2 TTS and speaker embedding networks in a self-supervised fashion. We hypothesize that the embeddings will contain minimal phonetic information since the TTS decoder will obtai…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.11221v1-abstract-full').style.display = 'inline'; document.getElementById('2010.11221v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2010.11221v1-abstract-full" style="display: none;">
       
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.11221v1-abstract-full').style.display = 'none'; document.getElementById('2010.11221v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 21 October, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> October 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2010.10694">arXiv:2010.10694</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2010.10694">pdf</a>, <a href="https://arxiv.org/format/2010.10694">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            An Investigation of the Relation Between Grapheme Embeddings and Pronunciation for <span class="search-hit mathjax">Tacotron</span>-based Systems
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Perquin%2C+A">Antoine Perquin</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Cooper%2C+E">Erica Cooper</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Yamagishi%2C+J">Junichi Yamagishi</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2010.10694v2-abstract-short" style="display: inline;">
            End-to-end models, particularly <span class="search-hit mathjax">Tacotron</span>-based ones, are currently a popular solution for text-to-speech synthesis. They allow the production of high-quality synthesized speech with little to no text preprocessing. Indeed, they can be trained using either graphemes or phonemes as input directly. However, in the case of grapheme inputs, little is known concer…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.10694v2-abstract-full').style.display = 'inline'; document.getElementById('2010.10694v2-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2010.10694v2-abstract-full" style="display: none;">
            End-to-end models, particularly <span class="search-hit mathjax">Tacotron</span>-based ones, are currently a popular solution for text-to-speech synthesis. They allow the production of high-quality synthesized speech with little to no text preprocessing. Indeed, they can be trained using either graphemes or phonemes as input directly. However, in the case of grapheme inputs, little is known concerning the relation between the underlying representations learned by the model and word pronunciations. This work investigates this relation in the case of a <span class="search-hit mathjax">Tacotron</span> model trained on French graphemes. Our analysis shows that grapheme embeddings are related to phoneme information despite no such information being present during training. Thanks to this property, we show that grapheme embeddings learned by <span class="search-hit mathjax">Tacotron</span> models can be useful for tasks such as grapheme-to-phoneme conversion and control of the pronunciation in synthetic speech.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.10694v2-abstract-full').style.display = 'none'; document.getElementById('2010.10694v2-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 4 April, 2021; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 20 October, 2020;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> October 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Submitted to Interspeech 2021</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2010.04301">arXiv:2010.04301</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2010.04301">pdf</a>, <a href="https://arxiv.org/format/2010.04301">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Non-Attentive <span class="search-hit mathjax">Tacotron</span>: Robust and Controllable Neural TTS Synthesis Including Unsupervised Duration Modeling
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Shen%2C+J">Jonathan Shen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Jia%2C+Y">Ye Jia</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chrzanowski%2C+M">Mike Chrzanowski</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+Y">Yu Zhang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Elias%2C+I">Isaac Elias</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zen%2C+H">Heiga Zen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Wu%2C+Y">Yonghui Wu</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2010.04301v4-abstract-short" style="display: inline;">
            This paper presents Non-Attentive <span class="search-hit mathjax">Tacotron</span> based on the…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.04301v4-abstract-full').style.display = 'inline'; document.getElementById('2010.04301v4-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2010.04301v4-abstract-full" style="display: none;">
            This paper presents Non-Attentive <span class="search-hit mathjax">Tacotron</span> based on the <span class="search-hit mathjax">Tacotron</span> 2 text-to-speech model, replacing the attention mechanism with an explicit duration predictor. This improves robustness significantly as measured by unaligned duration ratio and word deletion rate, two metrics introduced in this paper for large-scale robustness evaluation using a pre-trained speech recognition model. With the use of Gaussian upsampling, Non-Attentive <span class="search-hit mathjax">Tacotron</span> achieves a 5-scale mean opinion score for naturalness of 4.41, slightly outperforming <span class="search-hit mathjax">Tacotron</span> 2. The duration predictor enables both utterance-wide and per-phoneme control of duration at inference time. When accurate target durations are scarce or unavailable in the training data, we propose a method using a fine-grained variational auto-encoder to train the duration predictor in a semi-supervised or unsupervised manner, with results almost as good as supervised training.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2010.04301v4-abstract-full').style.display = 'none'; document.getElementById('2010.04301v4-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 11 May, 2021; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 8 October, 2020;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> October 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2009.06775">arXiv:2009.06775</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2009.06775">pdf</a>, <a href="https://arxiv.org/format/2009.06775">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Controllable neural text-to-speech synthesis using intuitive prosodic features
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Raitio%2C+T">Tuomo Raitio</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Rasipuram%2C+R">Ramya Rasipuram</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Castellani%2C+D">Dan Castellani</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2009.06775v1-abstract-short" style="display: inline;">
            …and spectral tilt can effectively control each prosodic dimension and generate a wide variety of speaking styles, while maintaining similar mean opinion score (4.23) to our <span class="search-hit mathjax">Tacotron</span> baseline (4.26).
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2009.06775v1-abstract-full').style.display = 'inline'; document.getElementById('2009.06775v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2009.06775v1-abstract-full" style="display: none;">
            Modern neural text-to-speech (TTS) synthesis can generate speech that is indistinguishable from natural speech. However, the prosody of generated utterances often represents the average prosodic style of the database instead of having wide prosodic variation. Moreover, the generated prosody is solely defined by the input text, which does not allow for different styles for the same sentence. In this work, we train a sequence-to-sequence neural network conditioned on acoustic speech features to learn a latent prosody space with intuitive and meaningful dimensions. Experiments show that a model conditioned on sentence-wise pitch, pitch range, phone duration, energy, and spectral tilt can effectively control each prosodic dimension and generate a wide variety of speaking styles, while maintaining similar mean opinion score (4.23) to our <span class="search-hit mathjax">Tacotron</span> baseline (4.26).
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2009.06775v1-abstract-full').style.display = 'none'; document.getElementById('2009.06775v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 14 September, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> September 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Accepted for publication in Interspeech 2020</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2009.05748">arXiv:2009.05748</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2009.05748">pdf</a>, <a href="https://arxiv.org/format/2009.05748">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Artificial Intelligence">cs.AI</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Visual-speech Synthesis of Exaggerated Corrective Feedback
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Bu%2C+Y">Yaohua Bu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+W">Weijun Li</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ma%2C+T">Tianyi Ma</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Chen%2C+S">Shengqi Chen</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Jia%2C+J">Jia Jia</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+K">Kun Li</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Lu%2C+X">Xiaobo Lu</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2009.05748v2-abstract-short" style="display: inline;">
            …visual-speech feedback in computer-assisted pronunciation training (CAPT). The speech exaggeration is realized by an emphatic speech generation neural network based on <span class="search-hit mathjax">Tacotron</span>, while the visual exaggeration is accomplished by ADC Viseme Blending, namely increasing Amplitude of movement, extending the phone's Duration and enhancing the color Contrast. Us…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2009.05748v2-abstract-full').style.display = 'inline'; document.getElementById('2009.05748v2-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2009.05748v2-abstract-full" style="display: none;">
            To provide more discriminative feedback for the second language (L2) learners to better identify their mispronunciation, we propose a method for exaggerated visual-speech feedback in computer-assisted pronunciation training (CAPT). The speech exaggeration is realized by an emphatic speech generation neural network based on <span class="search-hit mathjax">Tacotron</span>, while the visual exaggeration is accomplished by ADC Viseme Blending, namely increasing Amplitude of movement, extending the phone's Duration and enhancing the color Contrast. User studies show that exaggerated feedback outperforms non-exaggerated version on helping learners with pronunciation identification and pronunciation improvement.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2009.05748v2-abstract-full').style.display = 'none'; document.getElementById('2009.05748v2-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 15 December, 2020; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 12 September, 2020;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> September 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2008.05809">arXiv:2008.05809</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2008.05809">pdf</a>, <a href="https://arxiv.org/format/2008.05809">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Enhancing Speech Intelligibility in Text-To-Speech Synthesis using Speaking Style Conversion
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Paul%2C+D">Dipjyoti Paul</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Shifas%2C+M+P">Muhammed PV Shifas</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Pantazis%2C+Y">Yannis Pantazis</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Stylianou%2C+Y">Yannis Stylianou</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2008.05809v1-abstract-short" style="display: inline;">
            …in TTS synthesis, yet degraded synthesized quality often leads to worse intelligibility. To overcome such limitations, we proposed a novel transfer learning approach using <span class="search-hit mathjax">Tacotron</span> and WaveRNN based TTS synthesis. The proposed speech system exploits two modification strategies: (a) Lombard speaking style data and (b) Spectral Shaping and Dynamic Range Compre…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.05809v1-abstract-full').style.display = 'inline'; document.getElementById('2008.05809v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2008.05809v1-abstract-full" style="display: none;">
            The increased adoption of digital assistants makes text-to-speech (TTS) synthesis systems an indispensable feature of modern mobile devices. It is hence desirable to build a system capable of generating highly intelligible speech in the presence of noise. Past studies have investigated style conversion in TTS synthesis, yet degraded synthesized quality often leads to worse intelligibility. To overcome such limitations, we proposed a novel transfer learning approach using <span class="search-hit mathjax">Tacotron</span> and WaveRNN based TTS synthesis. The proposed speech system exploits two modification strategies: (a) Lombard speaking style data and (b) Spectral Shaping and Dynamic Range Compression (SSDRC) which has been shown to provide high intelligibility gains by redistributing the signal energy on the time-frequency domain. We refer to this extension as Lombard-SSDRC TTS system. Intelligibility enhancement as quantified by the Intelligibility in Bits (SIIB-Gauss) measure shows that the proposed Lombard-SSDRC TTS system shows significant relative improvement between 110% and 130% in speech-shaped noise (SSN), and 47% to 140% in competing-speaker noise (CSN) against the state-of-the-art TTS approach. Additional subjective evaluation shows that Lombard-SSDRC TTS successfully increases the speech intelligibility with relative improvement of 455% for SSN and 104% for CSN in median keyword correction rate compared to the baseline TTS method.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.05809v1-abstract-full').style.display = 'none'; document.getElementById('2008.05809v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 13 August, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Accepted in INTERSPEECH 2020</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2008.05284">arXiv:2008.05284</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2008.05284">pdf</a>, <a href="https://arxiv.org/format/2008.05284">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
            
              <div class="is-inline-block" style="margin-left: 0.5rem">
                <div class="tags has-addons">
                  <span class="tag is-dark is-size-7">doi</span>
                  <span class="tag is-light is-size-7"><a class="" href="https://doi.org/10.1109/LSP.2020.3016564">10.1109/LSP.2020.3016564 <i class="fa fa-external-link" aria-hidden="true"></i></a></span>
                </div>
              </div>
            
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Modeling Prosodic Phrasing with Multi-Task Learning in <span class="search-hit mathjax">Tacotron</span>-based TTS
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Liu%2C+R">Rui Liu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Sisman%2C+B">Berrak Sisman</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Bao%2C+F">Feilong Bao</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Gao%2C+G">Guanglai Gao</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+H">Haizhou Li</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2008.05284v1-abstract-short" style="display: inline;">
            <span class="search-hit mathjax">Tacotron</span>-based end-to-end speech synthesis has shown remarkable voice quality. However, the rendering of prosody in the synthesized speech remains to be improved, especially for long sentences, where prosodic phrasing errors can occur frequently. In this paper, we extend the…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.05284v1-abstract-full').style.display = 'inline'; document.getElementById('2008.05284v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2008.05284v1-abstract-full" style="display: none;">
            <span class="search-hit mathjax">Tacotron</span>-based end-to-end speech synthesis has shown remarkable voice quality. However, the rendering of prosody in the synthesized speech remains to be improved, especially for long sentences, where prosodic phrasing errors can occur frequently. In this paper, we extend the <span class="search-hit mathjax">Tacotron</span>-based speech synthesis framework to explicitly model the prosodic phrase breaks. We propose a multi-task learning scheme for <span class="search-hit mathjax">Tacotron</span> training, that optimizes the system to predict both Mel spectrum and phrase breaks. To our best knowledge, this is the first implementation of multi-task learning for <span class="search-hit mathjax">Tacotron</span> based TTS with a prosodic phrasing model. Experiments show that our proposed training scheme consistently improves the voice quality for both Chinese and Mongolian systems.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.05284v1-abstract-full').style.display = 'none'; document.getElementById('2008.05284v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 11 August, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">To appear in IEEE Signal Processing Letters (SPL)</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2008.03802">arXiv:2008.03802</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2008.03802">pdf</a>, <a href="https://arxiv.org/format/2008.03802">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Computation and Language">cs.CL</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            SpeedySpeech: Efficient Neural Speech Synthesis
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Vainer%2C+J">Jan Vainer</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Du%C5%A1ek%2C+O">Ondřej Dušek</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2008.03802v1-abstract-short" style="display: inline;">
            …teacher networks and use only a single attention layer in the teacher model. Coupled with a MelGAN vocoder, our model's voice quality was rated significantly higher than <span class="search-hit mathjax">Tacotron</span> 2. Our model can be efficiently trained on a single GPU and can run in real time even on a CPU. We provide both our source code and audio samples in our GitHub repository.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.03802v1-abstract-full').style.display = 'inline'; document.getElementById('2008.03802v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2008.03802v1-abstract-full" style="display: none;">
            While recent neural sequence-to-sequence models have greatly improved the quality of speech synthesis, there has not been a system capable of fast training, fast inference and high-quality audio synthesis at the same time. We propose a student-teacher network capable of high-quality faster-than-real-time spectrogram synthesis, with low requirements on computational resources and fast training time. We show that self-attention layers are not necessary for generation of high quality audio. We utilize simple convolutional blocks with residual connections in both student and teacher networks and use only a single attention layer in the teacher model. Coupled with a MelGAN vocoder, our model's voice quality was rated significantly higher than <span class="search-hit mathjax">Tacotron</span> 2. Our model can be efficiently trained on a single GPU and can run in real time even on a CPU. We provide both our source code and audio samples in our GitHub repository.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.03802v1-abstract-full').style.display = 'none'; document.getElementById('2008.03802v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 9 August, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">5 pages, 3 figures, Interspeech 2020</span>
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2008.02493">arXiv:2008.02493</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2008.02493">pdf</a>, <a href="https://arxiv.org/format/2008.02493">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            HooliGAN: Robust, High Quality Neural Vocoding
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=McCarthy%2C+O">Ollie McCarthy</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Ahmed%2C+Z">Zohaib Ahmed</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2008.02493v1-abstract-short" style="display: inline;">
            …results, finetunes very well to smaller datasets (&lt;30 minutes of speechdata) and generates audio at 2.2MHz on GPU and 35kHz on CPU. We also show a simple modification to <span class="search-hit mathjax">Tacotron</span>-basedmodels that allows seamless integration with HooliGAN. Results from our listening tests show the proposed model's ability to consistently output high-quality audio with…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.02493v1-abstract-full').style.display = 'inline'; document.getElementById('2008.02493v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2008.02493v1-abstract-full" style="display: none;">
            Recent developments in generative models have shown that deep learning combined with traditional digital signal processing (DSP) techniques could successfully generate convincing violin samples [1], that source-excitation combined with WaveNet yields high-quality vocoders [2, 3] and that generative adversarial network (GAN) training can improve naturalness [4, 5]. By combining the ideas in these models we introduce HooliGAN, a robust vocoder that has state of the art results, finetunes very well to smaller datasets (&lt;30 minutes of speechdata) and generates audio at 2.2MHz on GPU and 35kHz on CPU. We also show a simple modification to <span class="search-hit mathjax">Tacotron</span>-basedmodels that allows seamless integration with HooliGAN. Results from our listening tests show the proposed model's ability to consistently output high-quality audio with a variety of datasets, big and small. We provide samples at the following demo page: https://resemble-ai.github.io/hooligan_demo/
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.02493v1-abstract-full').style.display = 'none'; document.getElementById('2008.02493v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 6 August, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2008.02490">arXiv:2008.02490</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2008.02490">pdf</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            PPSpeech: Phrase based Parallel End-to-End TTS System
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Cong%2C+Y">Yahuan Cong</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Zhang%2C+R">Ran Zhang</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Luan%2C+J">Jian Luan</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2008.02490v1-abstract-short" style="display: inline;">
            Current end-to-end autoregressive TTS systems (e.g. <span class="search-hit mathjax">Tacotron</span> 2) have outperformed traditional parallel approaches on the quality of synthesized speech. However, they introduce new problems at the same time. Due to the autoregressive nature, the time cost of inference has to be proportional to the length of text, which pose a great challenge for online servin…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.02490v1-abstract-full').style.display = 'inline'; document.getElementById('2008.02490v1-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2008.02490v1-abstract-full" style="display: none;">
            Current end-to-end autoregressive TTS systems (e.g. <span class="search-hit mathjax">Tacotron</span> 2) have outperformed traditional parallel approaches on the quality of synthesized speech. However, they introduce new problems at the same time. Due to the autoregressive nature, the time cost of inference has to be proportional to the length of text, which pose a great challenge for online serving. On the other hand, the style of synthetic speech becomes unstable and may change obviously among sentences. In this paper, we propose a Phrase based Parallel End-to-End TTS System (PPSpeech) to address these issues. PPSpeech uses autoregression approach within a phrase and executes parallel strategies for different phrases. By this method, we can achieve both high quality and high efficiency. In addition, we propose acoustic embedding and text context embedding as the conditions of encoder to keep successive and prevent from abrupt style or timbre change. Experiments show that, the synthesis speed of PPSpeech is much faster than sentence level autoregressive <span class="search-hit mathjax">Tacotron</span> 2 when a sentence has more than 5 phrases. The speed advantage increases with the growth of sentence length. Subjective experiments show that the proposed system with acoustic embedding and context embedding as conditions can make the style transition across sentences gradient and natural, defeating Global Style Token (GST) obviously in MOS.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.02490v1-abstract-full').style.display = 'none'; document.getElementById('2008.02490v1-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 6 August, 2020; 
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2020.
          
        </p>
        
    
        
    
        
      </li>
    
      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2008.01490">arXiv:2008.01490</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2008.01490">pdf</a>, <a href="https://arxiv.org/format/2008.01490">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>
            
              
                <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Audio and Speech Processing">eess.AS</span>
              
            </div>
          
        </div>
        
        <p class="title is-5 mathjax">
          
            Expressive TTS Training with Frame and Style Reconstruction Loss
          
        </p>
        <p class="authors">
          <span class="has-text-black-bis has-text-weight-semibold">Authors:</span>
          
          <a href="/search/?searchtype=author&amp;query=Liu%2C+R">Rui Liu</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Sisman%2C+B">Berrak Sisman</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Gao%2C+G">Guanglai Gao</a>, 
          
          <a href="/search/?searchtype=author&amp;query=Li%2C+H">Haizhou Li</a>
          
        </p>
        
        <p class="abstract mathjax">
          <span class="search-hit">Abstract</span>:
          <span class="abstract-short has-text-grey-dark mathjax" id="2008.01490v2-abstract-short" style="display: inline;">
            We propose a novel training strategy for <span class="search-hit mathjax">Tacotron</span>-based text-to-speech (TTS) system to improve the expressiveness of speech. One of the key challenges in prosody modeling is the lack of reference that makes explicit modeling difficult. The proposed technique doesn't require prosody annotations from training data. It doesn't attempt to model prosody e…
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.01490v2-abstract-full').style.display = 'inline'; document.getElementById('2008.01490v2-abstract-short').style.display = 'none';">▽ More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2008.01490v2-abstract-full" style="display: none;">
            We propose a novel training strategy for <span class="search-hit mathjax">Tacotron</span>-based text-to-speech (TTS) system to improve the expressiveness of speech. One of the key challenges in prosody modeling is the lack of reference that makes explicit modeling difficult. The proposed technique doesn't require prosody annotations from training data. It doesn't attempt to model prosody explicitly either, but rather encodes the association between input text and its prosody styles using a <span class="search-hit mathjax">Tacotron</span>-based TTS framework. Our proposed idea marks a departure from the style token paradigm where prosody is explicitly modeled by a bank of prosody embeddings. The proposed training strategy adopts a combination of two objective functions: 1) frame level reconstruction loss, that is calculated between the synthesized and target spectral features; 2) utterance level style reconstruction loss, that is calculated between the deep style features of synthesized and target speech. The proposed style reconstruction loss is formulated as a perceptual loss to ensure that utterance level speech style is taken into consideration during training. Experiments show that the proposed training strategy achieves remarkable performance and outperforms a state-of-the-art baseline in both naturalness and expressiveness. To our best knowledge, this is the first study to incorporate utterance level perceptual quality as a loss function into <span class="search-hit mathjax">Tacotron</span> training for improved expressiveness.
            <a class="is-size-7" style="white-space: nowrap;" onclick="document.getElementById('2008.01490v2-abstract-full').style.display = 'none'; document.getElementById('2008.01490v2-abstract-short').style.display = 'inline';">△ Less</a>
          </span>
        </p>
        
    
        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 12 April, 2021; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 4 August, 2020;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> August 2020.
          
        </p>
        
        <p class="comments is-size-7">
          <span class="has-text-black-bis has-text-weight-semibold">Comments:</span>
          <span class="has-text-grey-dark mathjax">Submitted to IEEE/ACM Transactions on Audio, Speech and Language Processing</span>
        </p>
        
    
        
    
        
      </li>
    
    </ol>
    
    
      <nav class="pagination is-small is-centered breathe-horizontal" role="navigation" aria-label="pagination">
        
        <a href="" class="pagination-previous is-invisible">Previous
        </a>
        
        
          <a href="/search/?query=tacotron&amp;searchtype=all&amp;source=header&amp;order=-announced_date_first&amp;size=50&amp;abstracts=show&amp;start=50" class="pagination-next">Next
          </a>
        
        <ul class="pagination-list">
    
          <li>
            <a href="/search/?query=tacotron&amp;searchtype=all&amp;source=header&amp;order=-announced_date_first&amp;size=50&amp;abstracts=show&amp;start=0" class="pagination-link is-current" aria-label="Goto page 1">1
            </a>
          </li>
    
          
            
            <li>
              <a href="/search/?query=tacotron&amp;searchtype=all&amp;source=header&amp;order=-announced_date_first&amp;size=50&amp;abstracts=show&amp;start=50" class="pagination-link " aria-label="Page 2" aria-current="page">2
              </a>
            </li>
            
          
        </ul>
      </nav>
      
    
      
    
    
          <div class="is-hidden-tablet">
            <!-- feedback for mobile only -->
            <span class="help" style="display: inline-block;"><a href="https://github.com/arXiv/arxiv-search/releases">Search v0.5.6 released 2020-02-24</a>&nbsp;&nbsp;</span>
            <button class="button is-small" id="feedback-button">Feedback?</button>
          </div>
        </div>
   
</template>



