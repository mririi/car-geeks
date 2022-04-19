<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Update Question</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="row layout-top-spacing">
      <div class="col-xl-12 col-md-12 col-sm-12 col-12">
        <div class="panel-body">
          <div class="row">
            <div id="flRegistrationForm" class="col-lg-12 layout-spacing">
              <div class="statbox panel box box-shadow">
                <div class="panel-heading">
                  <div class="row">
                    <div class="col-xl-12 col-md-12 col-sm-12 col-12">
                      <h4>Update your Question</h4>
                    </div>
                  </div>
                </div>
                <div class="panel-body">
                  <b-form novalidate @submit.prevent="submit">
                    <label>Question title</label>
                    <b-form-group class="mb-3">
                      <b-input type="text" placeholder="Question title " v-model="form.titleQ" :class="[is_submit_form1 ? (form.titleQ && form.titleQ.length<100 && form.titleQ.length>15 ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.titleQ }">Please Enter content between 15 and 100 characters</b-form-invalid-feedback>
                    </b-form-group>
                    <label>Question details</label>
                    <b-form-group class="mb-3">
                      <b-textarea rows="4" type="text" v-model="form.contentQ" placeholder="Question details" :class="[is_submit_form1 ? (form.contentQ && form.contentQ.length<500 && form.contentQ.length>25 ? 'is-valid' : 'is-invalid') : '']"></b-textarea>
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.contentQ }">Please Enter content between 25 and 500 characters</b-form-invalid-feedback>
                    </b-form-group>
                    <label>Question image</label>
                    <div class="mb-4">
                      <b-file @change="onFileChanged"></b-file>
                    </div>
                    <label>Question Category</label>
                    <b-select value="Default select" v-model="form.categoryQ">
                      <b-select-option v-for="c in Questioncategories" :key="c.id" :value="c.id">{{ c.typeC }}</b-select-option>
                    </b-select>
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.categoryQ }">Please fill the Category</b-form-invalid-feedback>
                    <b-button @click="submit" variant="primary" class="mt-4 col-lg-3 ">Submit</b-button>
                  </b-form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.layout-px-spacing {
  min-height: calc(100vh - 170px) !important;
}
</style>
<script>
import moment from 'moment';
import Vue from 'vue';
import axios from 'axios';
Vue.filter('formatDate', function (value) {
  if (value) {
    return moment(String(value)).format('DD MMMM YYYY H:mm');
  }
});
import '@/assets/sass/components/cards/card.scss';
import '@/assets/sass/forms/file-upload-with-preview.min.css';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'Questions',
  components: {},
  data() {
    return {
      form: {
        titleQ: '',
        contentQ: '',
        userprofileQ: '',
        userentrepriseQ:'',
        categoryQ: 0,
      },
      image: null,
      uprofile: [],
      CurrentUser: [],
      is_submit_form1: false,
    };
  },
  created: function () {
    this.GetUsers();
    this.GetUserprofiles();
    this.GetQuestioncategories();
    this.GetUserentreprises()
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    
    axios.get('/question/question-detail/' + this.$route.params.id + '/').then((response) => {
      this.form = response.data;
    let existuserentreprise=false
      for (let ue in this.Userentreprises){
      if(this.Userentreprises[ue].userE==this.CurrentUser.id)
        {
          existuserentreprise = true
          if(this.Userentreprises[ue].id!=this.form.userentrepriseQ){
          this.$router.push('/questions')
          this.$swal({
              title: 'This is not your Question !',
              padding: '2em'
          });}
        }
      }
      if (existuserentreprise==false){
        let existuserprofile=false
      for (let uu in this.Userprofiles){
      if(this.Userprofiles[uu].userU==this.CurrentUser.id)
        {
          if(this.Userprofiles[uu].id!=this.form.userprofileQ){
            this.$router.push('/questions')
            this.$swal({
              
              title: 'This is not your Question !',
              padding: '2em'
          });
          }
          existuserprofile = true
        }
      }
      if (existuserprofile==false && existuserentreprise==false){
        this.$router.push('/auth/userinfo')
      }
      }});
  },
  methods: {
    onFileChanged(event) {
      this.image = event.target.files[0];
      console.log(this.image);
    },
    ...mapActions(['GetUserentreprises','CreateNotification','GetQuestioncategories', 'CreateQuestion', 'GetUsers', 'GetUserprofiles']),
    async submit() {
      try {
        this.is_submit_form1 = true;
                if (this.form.titleQ && this.form.titleQ.length<100 && this.form.titleQ.length>15 &&
                  this.form.contentQ && this.form.contentQ.length<500 && this.form.contentQ.length>25 
                ) {
        var formdata = new FormData();
        if (this.image != null) {
          formdata.append('imageQ', this.image);
        }
        formdata.append('titleQ', this.form.titleQ);
        formdata.append('contentQ', this.form.contentQ);
        formdata.append('categoryQ', this.form.categoryQ);
        if (this.CurrentUser.is_superuser){
        formdata.append("accepted", true);
        }else{
          formdata.append("accepted", false);
        }
        formdata.append('modified', true);
        axios.put('/question/question-update/' + this.$route.params.id + '/', formdata);
        if (this.CurrentUser.is_superuser==false){
        await this.CreateNotification({message:' requested a Verification on their question !',byuserprofileNo:this.form.userprofileQ,byuserentrepriseNo:this.form.userentrepriseQ,questionNo:1,foradmin:true})
        this.$swal('Good Job!', 'Your question has been updated successfuly, Please wait for the administator to accept it !', 'success');
        }
        this.$router.push('/questions');
        }
      } catch (error) {
        throw 'Il ya un error!';
      }
    },
  },
  computed: {
    ...mapGetters({Userentreprises:'StateUserentreprises', Questioncategories: 'StateQuestioncategories', Userprofiles: 'StateUserprofiles', User: 'StateUser', Users: 'StateUsers' }),
    isLoggedIn: function () {
      return this.$store.getters.isAuthenticated;
    },
  },
};
</script>