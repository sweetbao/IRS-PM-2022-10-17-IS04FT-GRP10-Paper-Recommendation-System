
<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, ref } from 'vue'
import PaperRecommend from '../components/PaperRecommend.vue';
import router from '../router'
import { useRoute } from 'vue-router'






export default {
  name: 'PaperView',
  props:['keywords'],
  components: {
    PaperRecommend
  },
  methods:{
    GetURL() {
      window.scrollTo(0, 0);
}
  },

  setup() {
    let base_url = "http://127.0.0.1:8000/api/"
    const route = useRoute();

    const state = reactive({
      Paper_list: [],
      SelectPapers: [],
    });

    const Getpaperlist = () => {
      axios.get(base_url + "testId/", state.SelectPapers).then(res  => {
            conslog.log(res)
          }).catch(err => {
            console.log(err)
          });
    };

    onMounted(() => {
      let selecttopic = route.params.keywords;
      const myArray = selecttopic.split(",");
      state.SelectPapers = myArray;
      Getpaperlist();
    });

    return {
      ...toRefs(state),
      Getpaperlist
    }
    
  }
  
}
</script>

<style>
:root { scroll-behavior: smooth; }
.stt {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  background: rgb(128, 128, 255) url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 384 512'%3E%3Cpath fill='currentColor' d='M352 352c-8.188 0-16.38-3.125-22.62-9.375L192 205.3l-137.4 137.4c-12.5 12.5-32.75 12.5-45.25 0s-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25C368.4 348.9 360.2 352 352 352z'%3E%3C/path%3E%3C/svg%3E") center no-repeat;
  box-shadow: 0 0.25rem 0.5rem 0 gray;
  opacity: 0.7;
}
.stt:hover {
  opacity: 0.8;
}
.stt:focus {
  opacity: 0.9;
}
.stt:active {
  opacity: 1;
}

</style>
<template>

<div>{{ SelectPapers }}</div>

  <div class="content" id="top">
    <ol class="breathe-horizontal" start="1">


      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2209.14698">arXiv:2209.14698</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2209.14698">pdf</a>, <a
                href="https://arxiv.org/format/2209.14698">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top"
              data-tooltip="Computer Vision and Pattern Recognition">cs.CV</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>

            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Networking and Internet Architecture">cs.NI</span>

            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Social and Information Networks">cs.SI</span>

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
          <span class="abstract-short has-text-grey-dark mathjax" id="2209.14698v1-abstract-short"
            style="display: inline;">
            This research aims to make metaverse characters more realistic by adding lip animations learnt from videos
            in the wild. To achieve this, our approach is to extend <span class="search-hit mathjax">Tacotron</span> 2
            text-to-speech synthesizer to generate lip movements together with mel spectrogram in one pass. The encoder
            and gate layer weights are pre-trained on LJ Speech 1.1 data set while the dec…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2209.14698v1-abstract-full').style.display = 'inline'; document.getElementById('2209.14698v1-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2209.14698v1-abstract-full" style="display: none;">
            This research aims to make metaverse characters more realistic by adding lip animations learnt from videos
            in the wild. To achieve this, our approach is to extend <span class="search-hit mathjax">Tacotron</span> 2
            text-to-speech synthesizer to generate lip movements together with mel spectrogram in one pass. The encoder
            and gate layer weights are pre-trained on LJ Speech 1.1 data set while the decoder is retrained on 93 clips
            of TED talk videos extracted from LRS 3 data set. Our novel decoder predicts displacement in 20 lip landmark
            positions across time, using labels automatically extracted by OpenFace 2.0 landmark predictor. Training
            converged in 7 hours using less than 5 minutes of video. We conducted ablation study for Pre/Post-Net and
            pre-trained encoder weights to demonstrate the effectiveness of transfer learning between audio and visual
            speech data.
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2209.14698v1-abstract-full').style.display = 'none'; document.getElementById('2209.14698v1-abstract-short').style.display = 'inline';">△
              Less</a>
          </span>
        </p>


        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 29 September,
          2022;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> September 2022.

        </p>



        <p class="comments is-size-7">

          <span class="has-text-black-bis has-text-weight-semibold">Report number:</span>
          This paper appears in the Proceedings of 2022 IEEE 8th World Forum on Internet of Things (WF-IoT). Please feel
          free to contact us for questions or remarks





        </p>



      </li>

      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2208.13183">arXiv:2208.13183</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2208.13183">pdf</a>, <a
                href="https://arxiv.org/format/2208.13183">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Audio and Speech Processing">eess.AS</span>

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
          <span class="abstract-short has-text-grey-dark mathjax" id="2208.13183v1-abstract-short"
            style="display: inline;">
            …on data generated by a less robust TTS system designed for a high-quality transfer task; in particular, a
            CHiVE-BERT monolingual TTS system is trained on the output of a <span
              class="search-hit mathjax">Tacotron</span> model designed for accent transfer. While some quality loss is
            inevitable with this approach, experimental results show that the models trained on synthetic data this way
            can produc…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2208.13183v1-abstract-full').style.display = 'inline'; document.getElementById('2208.13183v1-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2208.13183v1-abstract-full" style="display: none;">
            Transfer tasks in text-to-speech (TTS) synthesis - where one or more aspects of the speech of one set of
            speakers is transferred to another set of speakers that do not feature these aspects originally - remains a
            challenging task. One of the challenges is that models that have high-quality transfer capabilities can have
            issues in stability, making them impractical for user-facing critical tasks. This paper demonstrates that
            transfer can be obtained by training a robust TTS system on data generated by a less robust TTS system
            designed for a high-quality transfer task; in particular, a CHiVE-BERT monolingual TTS system is trained on
            the output of a <span class="search-hit mathjax">Tacotron</span> model designed for accent transfer. While
            some quality loss is inevitable with this approach, experimental results show that the models trained on
            synthetic data this way can produce high quality audio displaying accent transfer, while preserving speaker
            characteristics such as speaking style.
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2208.13183v1-abstract-full').style.display = 'none'; document.getElementById('2208.13183v1-abstract-short').style.display = 'inline';">△
              Less</a>
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
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2206.07373">pdf</a>, <a
                href="https://arxiv.org/format/2206.07373">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top"
              data-tooltip="Computation and Language">cs.CL</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>

            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Audio and Speech Processing">eess.AS</span>

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
          <span class="abstract-short has-text-grey-dark mathjax" id="2206.07373v1-abstract-short"
            style="display: inline;">
            NatiQ is end-to-end text-to-speech system for Arabic. Our speech synthesizer uses an encoder-decoder
            architecture with attention. We used both <span class="search-hit mathjax">tacotron</span>-based models
            (<span class="search-hit mathjax">tacotron</span>-1 and <span class="search-hit mathjax">tacotron</span>-2)
            and the faster transformer model for generating mel-spectrograms from characters. We co…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2206.07373v1-abstract-full').style.display = 'inline'; document.getElementById('2206.07373v1-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2206.07373v1-abstract-full" style="display: none;">
            NatiQ is end-to-end text-to-speech system for Arabic. Our speech synthesizer uses an encoder-decoder
            architecture with attention. We used both <span class="search-hit mathjax">tacotron</span>-based models
            (<span class="search-hit mathjax">tacotron</span>-1 and <span class="search-hit mathjax">tacotron</span>-2)
            and the faster transformer model for generating mel-spectrograms from characters. We concatenated Tacotron1
            with the WaveRNN vocoder, Tacotron2 with the WaveGlow vocoder and ESPnet transformer with the parallel
            wavegan vocoder to synthesize waveforms from the spectrograms. We used in-house speech data for two voices:
            1) neutral male "Hamza"- narrating general content and news, and 2) expressive female "Amina"- narrating
            children story books to train our models. Our best systems achieve an average Mean Opinion Score (MOS) of
            4.21 and 4.40 for Amina and Hamza respectively. The objective evaluation of the systems using word and
            character error rate (WER and CER) as well as the response time measured by real-time factor favored the
            end-to-end architecture ESPnet. NatiQ demo is available on-line at https://tts.qcri.org
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2206.07373v1-abstract-full').style.display = 'none'; document.getElementById('2206.07373v1-abstract-short').style.display = 'inline';">△
              Less</a>
          </span>
        </p>


        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 15 June, 2022;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> June 2022.

        </p>





      </li>

      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2204.04127">arXiv:2204.04127</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2204.04127">pdf</a>, <a
                href="https://arxiv.org/format/2204.04127">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top"
              data-tooltip="Audio and Speech Processing">eess.AS</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>

            <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>

          </div>


          <div class="is-inline-block" style="margin-left: 0.5rem">
            <div class="tags has-addons">
              <span class="tag is-dark is-size-7">doi</span>
              <span class="tag is-light is-size-7"><a class=""
                  href="https://doi.org/10.21437/Interspeech.2022-10446">10.21437/Interspeech.2022-10446 <i
                    class="fa fa-external-link" aria-hidden="true"></i></a></span>
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
          <span class="abstract-short has-text-grey-dark mathjax" id="2204.04127v2-abstract-short"
            style="display: inline;">
            …on singing data and depend on either error-prone time-alignment and duration features or explicit music
            score information. In this paper, we propose Karaoker, a multispeaker <span
              class="search-hit mathjax">Tacotron</span>-based model conditioned on voice characteristic features that
            is trained exclusively on spoken data without requiring time-alignments. Karaoker synthesizes singing voice
            and tra…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2204.04127v2-abstract-full').style.display = 'inline'; document.getElementById('2204.04127v2-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2204.04127v2-abstract-full" style="display: none;">
            Existing singing voice synthesis models (SVS) are usually trained on singing data and depend on either
            error-prone time-alignment and duration features or explicit music score information. In this paper, we
            propose Karaoker, a multispeaker <span class="search-hit mathjax">Tacotron</span>-based model conditioned on
            voice characteristic features that is trained exclusively on spoken data without requiring time-alignments.
            Karaoker synthesizes singing voice and transfers style following a multi-dimensional template extracted from
            a source waveform of an unseen singer/speaker. The model is jointly conditioned with a single deep
            convolutional encoder on continuous data including pitch, intensity, harmonicity, formants, cepstral peak
            prominence and octaves. We extend the text-to-speech training objective with feature reconstruction,
            classification and speaker identification tasks that guide the model to an accurate result. In addition to
            multitasking, we also employ a Wasserstein GAN training scheme as well as new losses on the acoustic model's
            output to further refine the quality of the model.
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2204.04127v2-abstract-full').style.display = 'none'; document.getElementById('2204.04127v2-abstract-short').style.display = 'inline';">△
              Less</a>
          </span>
        </p>


        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 31 August, 2022;
          <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 8 April, 2022;
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
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2204.03421">pdf</a>, <a
                href="https://arxiv.org/ps/2204.03421">ps</a>, <a
                href="https://arxiv.org/format/2204.03421">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>

            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Audio and Speech Processing">eess.AS</span>

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
          <span class="abstract-short has-text-grey-dark mathjax" id="2204.03421v1-abstract-short"
            style="display: inline;">
            …identity and to make them robust to noise and acoustic conditions. The learned features are used as
            pre-trained utterance-level embeddings and as inputs to a Non-Attentive <span
              class="search-hit mathjax">Tacotron</span> based architecture, aiming to achieve multispeaker speech
            synthesis without utilizing additional speaker features. This method enables us to train our model in an
            unlabeled multis…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2204.03421v1-abstract-full').style.display = 'inline'; document.getElementById('2204.03421v1-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2204.03421v1-abstract-full" style="display: none;">
            Voice cloning is a difficult task which requires robust and informative features incorporated in a high
            quality TTS system in order to effectively copy an unseen speaker's voice. In our work, we utilize features
            learned in a self-supervised framework via the Bootstrap Your Own Latent (BYOL) method, which is shown to
            produce high quality speech representations when specific audio augmentations are applied to the vanilla
            algorithm. We further extend the augmentations in the training procedure to aid the resulting features to
            capture the speaker identity and to make them robust to noise and acoustic conditions. The learned features
            are used as pre-trained utterance-level embeddings and as inputs to a Non-Attentive <span
              class="search-hit mathjax">Tacotron</span> based architecture, aiming to achieve multispeaker speech
            synthesis without utilizing additional speaker features. This method enables us to train our model in an
            unlabeled multispeaker dataset as well as use unseen speaker embeddings to copy a speaker's voice.
            Subjective and objective evaluations are used to validate the proposed model, as well as the robustness to
            the acoustic conditions of the target utterance.
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2204.03421v1-abstract-full').style.display = 'none'; document.getElementById('2204.03421v1-abstract-short').style.display = 'inline';">△
              Less</a>
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
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2204.01115">pdf</a>, <a
                href="https://arxiv.org/format/2204.01115">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Human-Computer Interaction">cs.HC</span>

            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Audio and Speech Processing">eess.AS</span>

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
          <span class="abstract-short has-text-grey-dark mathjax" id="2204.01115v1-abstract-short"
            style="display: inline;">
            …convex combinations were investigated for the generation of higher competence in female speech. We have
            employed a feature quantization approach in the traditional end-to-end <span
              class="search-hit mathjax">tacotron</span> based speech synthesis model. The listening tests have shown
            that the convex combination of acoustic features displays higher Mean Opinion Scores of warmth and
            competence when…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2204.01115v1-abstract-full').style.display = 'inline'; document.getElementById('2204.01115v1-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2204.01115v1-abstract-full" style="display: none;">
            In our previous work, we derived the acoustic features, that contribute to the perception of warmth and
            competence in synthetic speech. As an extension, in our current work, we investigate the impact of the
            derived vocal features in the generation of the desired characteristics. The acoustic features, spectral
            flux, F1 mean and F2 mean and their convex combinations were explored for the generation of higher warmth in
            female speech. The voiced slope, spectral flux, and their convex combinations were investigated for the
            generation of higher competence in female speech. We have employed a feature quantization approach in the
            traditional end-to-end <span class="search-hit mathjax">tacotron</span> based speech synthesis model. The
            listening tests have shown that the convex combination of acoustic features displays higher Mean Opinion
            Scores of warmth and competence when compared to that of individual features.
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2204.01115v1-abstract-full').style.display = 'none'; document.getElementById('2204.01115v1-abstract-short').style.display = 'inline';">△
              Less</a>
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
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2203.02967">pdf</a>, <a
                href="https://arxiv.org/format/2203.02967">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Audio and Speech Processing">eess.AS</span>

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
          <span class="abstract-short has-text-grey-dark mathjax" id="2203.02967v1-abstract-short"
            style="display: inline;">
            …However, because of prosodic phrasing and large character set of Mandarin, Chinese utilization of these
            models is not yet complete. By creating a new dataset and replacing <span
              class="search-hit mathjax">Tacotron</span> synthesizer with VAENAR-TTS, we improved the existing speech
            cloning technique CV2TTS to almost real-time speech cloning while guaranteeing synthesis quality. In the
            process, we…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2203.02967v1-abstract-full').style.display = 'inline'; document.getElementById('2203.02967v1-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2203.02967v1-abstract-full" style="display: none;">
            Speech cloning technology is becoming more sophisticated thanks to the advances in machine learning.
            Researchers have successfully implemented natural-sounding English speech synthesis and good English speech
            cloning by some effective models. However, because of prosodic phrasing and large character set of Mandarin,
            Chinese utilization of these models is not yet complete. By creating a new dataset and replacing <span
              class="search-hit mathjax">Tacotron</span> synthesizer with VAENAR-TTS, we improved the existing speech
            cloning technique CV2TTS to almost real-time speech cloning while guaranteeing synthesis quality. In the
            process, we customized the subjective tests of synthesis quality assessment by attaching various scenarios,
            so that subjects focus on the differences between voice and our improvements maybe were more advantageous to
            practical applications. The results of the A/B test, real-time factor (RTF) and 2.74 mean opinion score
            (MOS) in terms of naturalness and similarity, reflect the real-time high-quality Mandarin speech cloning we
            achieved.
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2203.02967v1-abstract-full').style.display = 'none'; document.getElementById('2203.02967v1-abstract-short').style.display = 'inline';">△
              Less</a>
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
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2202.07907">pdf</a>, <a
                href="https://arxiv.org/format/2202.07907">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top" data-tooltip="Machine Learning">cs.LG</span>

            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Audio and Speech Processing">eess.AS</span>

          </div>

        </div>

        <p class="title is-5 mathjax">

          Singing-<span class="search-hit mathjax">Tacotron</span>: Global duration control attention and dynamic filter
          for End-to-end singing voice synthesis

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
          <span class="abstract-short has-text-grey-dark mathjax" id="2202.07907v1-abstract-short"
            style="display: inline;">
            …model instability or even failure to synthesize voice. To learn accurate alignment information
            automatically, this paper proposes an end-to-end SVS framework, named Singing-<span
              class="search-hit mathjax">Tacotron</span>. The main difference between the proposed framework and <span
              class="search-hit mathjax">Tacotron</span> is that the speech can be controlled significantly by the
            musical score&amp;#…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2202.07907v1-abstract-full').style.display = 'inline'; document.getElementById('2202.07907v1-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2202.07907v1-abstract-full" style="display: none;">
            End-to-end singing voice synthesis (SVS) is attractive due to the avoidance of pre-aligned data. However,
            the auto learned alignment of singing voice with lyrics is difficult to match the duration information in
            musical score, which will lead to the model instability or even failure to synthesize voice. To learn
            accurate alignment information automatically, this paper proposes an end-to-end SVS framework, named
            Singing-<span class="search-hit mathjax">Tacotron</span>. The main difference between the proposed framework
            and <span class="search-hit mathjax">Tacotron</span> is that the speech can be controlled significantly by
            the musical score's duration information. Firstly, we propose a global duration control attention mechanism
            for the SVS model. The attention mechanism can control each phoneme's duration. Secondly, a duration encoder
            is proposed to learn a set of global transition tokens from the musical score. These transition tokens can
            help the attention mechanism decide whether moving to the next phoneme or staying at each decoding step.
            Thirdly, to further improve the model's stability, a dynamic filter is designed to help the model overcome
            noise interference and pay more attention to local context information. Subjective and objective evaluation
            verify the effectiveness of the method. Furthermore, the role of global transition tokens and the effect of
            duration control are explored. Examples of experiments can be found at
            https://hairuo55.github.io/SingingTacotron.
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2202.07907v1-abstract-full').style.display = 'none'; document.getElementById('2202.07907v1-abstract-short').style.display = 'inline';">△
              Less</a>
          </span>
        </p>


        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 16 February,
          2022;
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
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2201.12567">pdf</a>, <a
                href="https://arxiv.org/format/2201.12567">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top" data-tooltip="Sound">cs.SD</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Audio and Speech Processing">eess.AS</span>

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
          <span class="abstract-short has-text-grey-dark mathjax" id="2201.12567v1-abstract-short"
            style="display: inline;">
            …ppg-based voice conversion model that adopts a fully end-to-end structure. Experimental results show that
            the proposed method outperforms other conversion models, including <span
              class="search-hit mathjax">Tacotron</span>-based and Fastspeech-based models, on conversion quality and
            spoofing performance against anti-spoofing systems. In addition, we investigate several post-processing
            methods for b…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2201.12567v1-abstract-full').style.display = 'inline'; document.getElementById('2201.12567v1-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2201.12567v1-abstract-full" style="display: none;">
            The voice conversion task is to modify the speaker identity of continuous speech while preserving the
            linguistic content. Generally, the naturalness and similarity are two main metrics for evaluating the
            conversion quality, which has been improved significantly in recent years. This paper presents the HCCL-DKU
            entry for the fake audio generation task of the 2022 ICASSP ADD challenge. We propose a novel ppg-based
            voice conversion model that adopts a fully end-to-end structure. Experimental results show that the proposed
            method outperforms other conversion models, including <span class="search-hit mathjax">Tacotron</span>-based
            and Fastspeech-based models, on conversion quality and spoofing performance against anti-spoofing systems.
            In addition, we investigate several post-processing methods for better spoofing power. Finally, we achieve
            second place with a deception success rate of 0.916 in the ADD challenge.
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2201.12567v1-abstract-full').style.display = 'none'; document.getElementById('2201.12567v1-abstract-short').style.display = 'inline';">△
              Less</a>
          </span>
        </p>


        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 29 January,
          2022;
          <span class="has-text-black-bis has-text-weight-semibold">originally announced</span> January 2022.

        </p>





      </li>

      <li class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a href="https://arxiv.org/abs/2201.10375">arXiv:2201.10375</a>
            <span>&nbsp;[<a href="https://arxiv.org/pdf/2201.10375">pdf</a>, <a
                href="https://arxiv.org/format/2201.10375">other</a>]&nbsp;</span>
          </p>
          <div class="tags is-inline-block">
            <span class="tag is-small is-link tooltip is-tooltip-top"
              data-tooltip="Audio and Speech Processing">eess.AS</span>


            <span class="tag is-small is-grey tooltip is-tooltip-top"
              data-tooltip="Computation and Language">cs.CL</span>

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
          <span class="abstract-short has-text-grey-dark mathjax" id="2201.10375v2-abstract-short"
            style="display: inline;">
            …is realized using an energy-based attention mechanism known as Dynamic Convolution Attention, in
            combination with a set of modifications proposed for the synthesizer based on <span
              class="search-hit mathjax">Tacotron</span> 2. Moreover, effective zero-shot speaker adaptation is achieved
            by conditioning both the synthesizer and vocoder on a speaker encoder that has been pretrained on a large
            corpus…
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2201.10375v2-abstract-full').style.display = 'inline'; document.getElementById('2201.10375v2-abstract-short').style.display = 'none';">▽
              More</a>
          </span>
          <span class="abstract-full has-text-grey-dark mathjax" id="2201.10375v2-abstract-full" style="display: none;">
            With recent advancements in voice cloning, the performance of speech synthesis for a target speaker has been
            rendered similar to the human level. However, autoregressive voice cloning systems still suffer from text
            alignment failures, resulting in an inability to synthesize long sentences. In this work, we propose a
            variant of attention-based text-to-speech system that can reproduce a target voice from a few seconds of
            reference speech and generalize to very long utterances as well. The proposed system is based on three
            independently trained components: a speaker encoder, synthesizer and universal vocoder. Generalization to
            long utterances is realized using an energy-based attention mechanism known as Dynamic Convolution
            Attention, in combination with a set of modifications proposed for the synthesizer based on <span
              class="search-hit mathjax">Tacotron</span> 2. Moreover, effective zero-shot speaker adaptation is achieved
            by conditioning both the synthesizer and vocoder on a speaker encoder that has been pretrained on a large
            corpus of diverse data. We compare several implementations of voice cloning systems in terms of speech
            naturalness, speaker similarity, alignment consistency and ability to synthesize long utterances, and
            conclude that the proposed model can produce intelligible synthetic speech for extremely long utterances,
            while preserving a high extent of naturalness and similarity for short texts.
            <a class="is-size-7" style="white-space: nowrap;"
              onclick="document.getElementById('2201.10375v2-abstract-full').style.display = 'none'; document.getElementById('2201.10375v2-abstract-short').style.display = 'inline';">△
              Less</a>
          </span>
        </p>


        <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted</span> 26 January,
          2022; <span class="has-text-black-bis has-text-weight-semibold">v1</span> submitted 25 January, 2022;
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
      <a @click="GetURL()" class="stt" title="Back to Top"></a>


    </ol>

  </div>

</template>



