<template>
  <div id="app">
    <ConversationalForm @submit="submit">
      <fieldset>
        <label for="age">What's your age?</label>
        <input required data-question="Hi there! What's your age? " type="text" name="age" id="age">
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
          <option value="1">Typical Angina</option>
          <option value="2">Atypical Angina</option>
          <option value="3">Non-Anginal Pain</option>
          <option value="4">Asymptomatic</option>
        </select>
      </fieldset>
      <fieldset>
        <label for="trtbps">What's your trtbps?</label>
        <input required data-question="What's your trtbps?" type="text" name="trtbps" id="trtbps">
      </fieldset>
      <fieldset>
        <label for="chol">What's your Cholesterol?</label>
        <input required data-question="What's your Cholesterol?" type="text" name="chol" id="chol">
      </fieldset>
      <fieldset>
        <label for="exng">Do you have exercise induce angina?</label><br />
        <input type="radio" data-question="Do you have exercise induce angina?" name="exng" value="1" data-text="Yes" /> Yes<br>
        <input type="radio" name="exng" value="0" data-text="No" /> No<br>
      </fieldset>
      <fieldset>
        <label for="fbs">Is your fasting blood sugar > 120 mg/dl?</label><br />
        <input type="radio" data-question="Is your fasting blood sugar > 120 mg/dl?" name="fbs" value="1" data-text="Yes" /> Yes<br>
        <input type="radio" name="fbs" value="0" data-text="No" /> No<br>
      </fieldset>
      <fieldset>
        <label for="restecg">Select an option about resting electrocardiographic results</label>
        <select data-question="Select an option about resting elfctrocardiographic results" name="restecg" id="restecg">
          <option></option>
          <option value="0">Normal</option>
          <option value="1">having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) </option>
          <option value="2"> showing probable or definite left ventricular hypertrophy by Estes' criteria</option>
        </select>
      </fieldset>
      <fieldset>
        <label for="oldpeak">Please enter your Old Peak</label>
        <input required data-question="Please enter your Old Peak" type="text" name="oldpeak" id="oldpeak">
      </fieldset>
      <fieldset>
        <label for="thalachh">What's your maximum heart rate you achieved?</label>
        <input required data-question="What's your maximum heart rate you achieved?" type="text" name="thalachh" id="thalachh">
      </fieldset>
      <fieldset>
      <label for="caa">How many major vessels do you have?</label>
      <select data-question="How many major vessels do you have?" name="caa" id="caa">
        <option></option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
      </select>
      </fieldset>
      <fieldset>
        <label for="thall">What's your Thal rate?</label>
        <input required data-question="What's your Thal rate?" type="text" name="thall" id="thall">
      </fieldset>
      <fieldset>
        <label for="thats-all">Are you ready to submit the form?</label>
        <button data-question="Are you ready to submit the form?" data-success="Submited! Yay! 😄" name="submit" type="submit" data-cancel="Nope">Yup</button>
      </fieldset>
    </ConversationalForm>
    <h1 v-if="predictedClass">Will You Have a Heart Attack??? The answer is: {{predictedClass}}</h1>
  </div>
</template>

<script>
import ConversationalForm from 'vue-conversational-form'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    ConversationalForm
  },
  data: () => ({
    predictedClass: ''
  }),
  methods: {
    submit(o) {
      console.log(o)
      axios.post("http://127.0.0.1:5000/predict",{
        age: o.age,
        sex: o.sex,
        cp: o.cp,
        trtbps: o.trtbps,
        chol: o.chol,
        fbs: o.fbs,
        restecg: o.restecg,
        thalachh: o.thalachh,
        exng: o.exng,
        oldpeak: o.oldpeak,
        caa: o.caa,
        thall: o.thall
      }).then((response) =>{
        if(response.data.class === 1){
          console.log(response.data.class)
          this.predictedClass = "Yeah Probably Lmao"
        }else{
          this.predictedClass = "No, you're chillin"
        }
      })
    }
  }
}
</script>

<style lang = sass>

</style>
