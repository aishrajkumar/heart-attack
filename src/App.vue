<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark

    >
      <v-spacer>
      <v-toolbar-title class="text-center">Heart Attack Prediction</v-toolbar-title>
      </v-spacer>
    </v-app-bar>

    <v-main>

      <div v-if="showResults === false">
        <ConversationalForm @submit="submit">
          <fieldset>
            <label for="temp">Temp</label><br />
            <input type="radio" data-question="Welcome! Please fill out this form to get a prediction on whether or not you are more likely to have a heart attack." name="temp" value="1" data-text="Start" /><br>
          </fieldset>
          <fieldset>
            <label for="sex">Gender</label><br />
            <input type="radio" data-question="What's your gender?" name="sex" value="1" data-text="Male" /> Male<br>
            <input type="radio" name="sex" value="0" data-text="Female" /> Female<br>
          </fieldset>
          <fieldset>
            <label for="cp">What type of chest pain are you having?</label>
            <select data-question="What type of chest pain are you having?" name="cp" id="cp">
              <option></option>
              <option value="0">Typical Angina</option>
              <option value="1">Atypical Angina</option>
              <option value="2">Non-Anginal Pain</option>
              <option value="3">Asymptomatic</option>
            </select>
          </fieldset>
          <fieldset>
            <label for="fbs">Is your fasting blood sugar > 120 mg/dl?</label><br />
            <input type="radio" data-question="Is your fasting blood sugar > 120 mg/dl?" name="fbs" value="1" data-text="Yes" /> Yes<br>
            <input type="radio" name="fbs" value="0" data-text="No" /> No<br>
          </fieldset>
          <fieldset>
            <label for="restecg">Select an option about resting electrocardiographic results</label>
            <select data-question="Select an option about resting electrocardiographic  results" name="restecg" id="restecg">
              <option></option>
              <option value="0">Normal</option>
              <option value="1">Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) </option>
              <option value="2"> Showing probable or definite left ventricular hypertrophy by Estes' criteria</option>
            </select>
          </fieldset>
          <fieldset>
            <label for="exng">Do you have exercise induce angina?</label><br />
            <input type="radio" data-question="Do you have exercise induce angina?" name="exng" value="1" data-text="Yes" /> Yes<br>
            <input type="radio" name="exng" value="0" data-text="No" /> No<br>
          </fieldset>


          <fieldset>
            <label for="oldpeak">What is your ST depression included by exercise relative to rest</label>
            <input required data-question="What is your ST depression included by exercise relative to rest?" type="text" name="oldpeak" id="oldpeak">
          </fieldset>
          <fieldset>
            <label for="slp"></label>
            <select data-question="What is your slop of the peak exercise ST segment?" name="slp" id="slp">
              <option value="0">Upsloping</option>
              <option value="1">Flat</option>
              <option value="2">Downsloping</option>
            </select>
          </fieldset>
          <fieldset>
            <label for="caa">How many major vessels do you have?</label>
            <select data-question="How many major vessels do you have?" name="caa" id="caa">
              <option>0</option>
              <option>1</option>
              <option>2</option>
              <option>3</option>
            </select>
          </fieldset>
          <fieldset>
            <label for="thats-all">Are you ready to submit the form?</label>
            <button data-question="Are you ready to submit the form?" data-success="Submited! Yay! 😄" name="submit" type="submit" data-cancel="Nope">Yup</button>
          </fieldset>
          <fieldset>
            <label for="thats-all">Want to start over?</label>
            <button data-question="Want to start over?" name="reset" type="reset" data-cancel="No">Yes, let's go again</button>
          </fieldset>
        </ConversationalForm>
      </div>
      <Plotly :data="data" :layout="layout" v-if="showResults === true"></Plotly>
      <v-spacer></v-spacer>
      <h1 v-if="showResults === true"  class="text-center">Are you more likely to have a heart attack?: {{predictedClass}}</h1>
      <div class="text-center" v-if="showResults === true">
      <v-btn class="ma-7" color= "rgba(134, 104, 231, 1)" @click="reloadPage">Start Over</v-btn>
      </div>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios'
import ConversationalForm from "vue-conversational-form"
import { Plotly } from 'vue-plotly'
import importance from "../public/model_importance.json"

export default {
  name: 'App',

  components: {
    ConversationalForm,
    Plotly,
  },
data: () => ({
  predictedClass: '',
  showResults: false,
  data: [{
    x: Object.keys(importance),
    y: Object.values(importance),
    type: "bar",
    marker: {
      color:  "rgba(134, 104, 231, 1)"
    }
  }],
  layout: {
    title: "Feature Importance"
  }
}),

  mounted() {
    this.init()
  },
  created() {
    this.importance = importance
  },



    methods: {
    init() {
    },
      reloadPage(){
        window.location.reload()
        this.showResults = false
      },
  submit(o) {
      console.log(o)
    axios.post("http://127.0.0.1:5000/predict",{
      sex: o.sex,
      cp: o.cp,
      fbs: o.fbs,
      restecg: o.restecg,
      exng: o.exng,
      oldpeak: o.oldpeak,
      slp: o.slp,
      caa: o.caa,
    }).then((response) =>{
      console.log(response.data.class)
      if(response.data.class === 1){
        this.predictedClass = "Yes seek medical attention."
      }else{
        this.predictedClass = "No, seek medical attention if condition worsens."
      }
    })
    this.showResults = true
  }
}
}
</script>

<style>
.vcf-container[data-v-6e22b156] {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  width: 1440px;
  height: 900px;
  max-width: 50000px;
  -webkit-box-orient: vertical;
  -moz-animation-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  margin: auto;
  background: #FAFAFA;
  font-family: "Cairo", sans-serif;
  line-height: 1.2rem;
  font-size: 1rem;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}


</style>

