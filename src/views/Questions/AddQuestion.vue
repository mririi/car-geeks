<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Add Question</span></li>
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
                    <div class="col-xl-10 col-md-12 col-sm-12 col-12">
                      <h4>Add Question</h4>
                    </div>
                  </div>
                </div>
                <div class="panel-body">
                  <b-form novalidate @submit.prevent="submit">
                    <label >Question title <span style="color:red">*</span></label>
                    <b-form-group class="mb-3">
                      <b-input type="text" placeholder="Question title " v-model="form.titleQ" :class="[is_submit_form1 ? (form.titleQ && form.titleQ.length<100 && form.titleQ.length>15 ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.titleQ  }">Please Enter a title between 15 and 100 characters</b-form-invalid-feedback>
                    </b-form-group>
                    <label >Question details <span style="color:red">*</span></label>
                    <b-form-group class="mb-3">
                      <b-textarea rows="4" type="text" v-model="form.contentQ" placeholder="Question details" :class="[is_submit_form1 ? (form.contentQ && form.contentQ.length<500 && form.contentQ.length>25 ? 'is-valid' : 'is-invalid') : '']"></b-textarea>
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.contentQ }">Please Enter content between 25 and 500 characters</b-form-invalid-feedback>
                    </b-form-group>
                    <label >Insert image</label>
                    <div class="mb-4">
                      <b-file @change="onFileChanged"></b-file>
                    </div>
                    <label >Select Category <span style="color:red">*</span></label>
                    <b-select value="Default select" v-model="form.categoryQ" >
                      <b-select-option value="0">Select Category</b-select-option>
                      <b-select-option v-for="c in Questioncategories" :key="c.id" :value="c.id">{{c.typeC}}</b-select-option>
                    </b-select>
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.categoryQ }">Please fill the Category</b-form-invalid-feedback>
               <!--      <vue-tags-input
      v-model="tag"
      :tags="tags"
      @tags-changed="newTags => tags = newTags"
    />-->
                     <small id="emailHelp2" class="form-text text-muted mt-3"><span style="color:red">*</span> Required Fields</small>
                    <b-button  @click="submit" variant="primary" class="mt-4 justfiy-content-end">Submit</b-button>
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
import '@/assets/sass/components/cards/card.scss';
import '@/assets/sass/forms/file-upload-with-preview.min.css';
import { mapGetters, mapActions } from 'vuex';
//import VueTagsInput from '@johmun/vue-tags-input';
import axios from 'axios'
export default {
  metaInfo: { title: 'Add Question' },
  components: {
   // VueTagsInput,
    },
  data() {
    return {
      tag: '',
      tags: [],
      form: {
        titleQ: '',
        contentQ: '',
        userprofileQ:'',
        userentrepriseQ:'',
        categoryQ:0,
        
      },
      image:null,
      uentreprise:[],
      uprofile:[],
      CurrentUser:[],
      is_submit_form1:false, 
    };
  },
  created: function() {
    this.GetUsers()
    this.GetUserprofiles()
    this.GetQuestioncategories()
    this.GetUserentreprises()
    this.GetQuestions()
    for (let u in this.Users){
      if(this.Users[u].username==this.User)
        {
          this.CurrentUser = this.Users[u];
        }
      }
      
      let existuserentreprise=false
      for (let ue in this.Userentreprises){
      if(this.Userentreprises[ue].userE==this.CurrentUser.id)
        {
          existuserentreprise = true
          this.uentreprise=this.Userentreprises[ue]
          this.form.userentrepriseQ=this.uentreprise.id
        }
      }
      if (existuserentreprise==false){
        let existuserprofile=false
      for (let uu in this.Userprofiles){
      if(this.Userprofiles[uu].userU==this.CurrentUser.id)
        {
          existuserprofile = true
          this.uprofile=this.Userprofiles[uu]
          this.form.userprofileQ=this.uprofile.id
          
        }
      }
      if (existuserprofile==false){
        this.$router.push('/auth/userinfo')
      }
      }
      
  },
    methods: {
   onFileChanged (event) {
      this.image = event.target.files[0]
    },
    ...mapActions(["GetUserentreprises",'GetQuestions','CreateNotification',"GetQuestioncategories","CreateQuestion","GetUsers","GetUserprofiles"]),
    async submit() {
      if(this.Questions.find((q)=>q.titleQ==this.form.titleQ)==null){
        this.is_submit_form1 = true;
                if (this.form.titleQ && this.form.titleQ.length<100 && this.form.titleQ.length>15 &&
                  this.form.contentQ && this.form.contentQ.length<500 && this.form.contentQ.length>25 &&
                  this.form.categoryQ
                ) {
      var formdata = new FormData();
      if (this.image!=null)
      {
        formdata.append("imageQ", this.image);
      }
        formdata.append("titleQ", this.form.titleQ);
        formdata.append("contentQ", this.form.contentQ);
        formdata.append("categoryQ", this.form.categoryQ);
        if (this.CurrentUser.is_superuser){
        formdata.append("accepted", true);
        axios.put('/userprofile/userprofile-update/'+this.form.userprofileQ+'/',{nbquestions:this.uprofile.nbquestions+1})
        }
        //formdata.append("tags", this.tags.text);
        formdata.append("userprofileQ", this.form.userprofileQ);
        formdata.append("userentrepriseQ", this.form.userentrepriseQ);
        this.CreateQuestion(formdata);
        if (this.CurrentUser.is_superuser==false){
          await this.CreateNotification({message:' requested a Verification on their question !',byuserprofileNo:this.form.userprofileQ,byuserentrepriseNo:this.form.userentrepriseQ,questionNo:1,foradmin:true})
        this.$swal('Good Job!', 'Your question has been created successfuly, Please wait for the administator to accept it !', 'success');
        }
        this.$router.push("/questions");
      }
      }else{
        let question=this.Questions.find((q)=>q.titleQ==this.form.titleQ)
        this.$swal.fire({
        title: 'This question already exists !',
        padding: '2em',
        html: '<a style="color:blue" href="/questionpage/'+question.id+'/'+question.slug+'/">Check it out!</a>',
        confirmButtonText: 'No thanks'
      })
      }
       }
    },
    computed: {
    ...mapGetters({Questions:"StateQuestions", Userentreprises:"StateUserentreprises",Questioncategories:"StateQuestioncategories",Userprofiles:"StateUserprofiles", User: "StateUser",Users: "StateUsers"}),
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
    },
};
</script>