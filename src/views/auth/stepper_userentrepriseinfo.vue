<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page"><span>Informations</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="row layout-top-spacing">
      <div class="col-xl-12 col-lg-12 col-md-12 col-12 layout-spacing">
        <div class="panel br-4">
          <div class="panel-body">
            <form-wizard title="" @on-complete="onComplete" subtitle="" shape="circle" color="#4361ee">
              <tab-content title="More Informations" icon="far fa-user">
                <b-form>
                  <b-form-row class="mb-4">
                    <b-form-group label="Name" class="col-md-4">
                      <b-input type="text" placeholder="Name" v-model="form.nameE" :class="[is_submit_form1 ? (form.nameE ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.nameE }">Please fill the name</b-form-invalid-feedback>
                    </b-form-group>
                    <b-form-group label="Business type" class="col-md-4">
                      <b-input type="text" placeholder="Business type" v-model="form.typeE" :class="[is_submit_form1 ? (form.typeE ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.typeE }">Please fill the Business type</b-form-invalid-feedback>
                    </b-form-group>
                     <b-form-group label="Phone Number" class="col-md-4">
                      <b-input type="number" placeholder="Phone number" v-model="form.contactE" :class="[is_submit_form1 ? (form.contactE ? 'is-valid' : 'is-invalid') : '']" />
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.contactE }">Please fill the Phone number</b-form-invalid-feedback>
                    </b-form-group>
                  </b-form-row>
                  <hr />
                  <b-form-row class="mb-4">
                    <b-form-group class="col-md-6" label="Address">
                      <b-input placeholder="1234 Main St" v-model="form.addressE"></b-input>
                    </b-form-group>
                    <b-form-group class="col-md-6" label="Country">
                      <country-select
                        class="country-select"
                        v-model="form.country"
                        :country="form.country"
                        countryName
                        topCountry="US"
                        :class="[is_submit_form1 ? (form.country ? 'is-valid' : 'is-invalid') : '']"
                      />
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.country }">Please fill the Country</b-form-invalid-feedback>
                    </b-form-group>
                  </b-form-row>
                  <hr />
                  <b-form-row class="mb-4">
                    <div class="custom-file-container col-6" data-upload-id="myFirstImage">
                      <label>Upload Logo <a href="javascript:void(0)" class="custom-file-container__image-clear" title="Clear Image">x</a></label>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !image }">Please fill the image !</b-form-invalid-feedback>
                    
                      <label class="custom-file-container__custom-file">
                        <input type="file" @change="onFileChanged" class="custom-file-container__custom-file__custom-file-input" accept="image/*" :class="[is_submit_form1 ? (image ? 'is-valid' : 'is-invalid') : '']" />
                        <input type="hidden" name="MAX_FILE_SIZE" value="10485760" />
                        <span class="custom-file-container__custom-file__custom-file-control"></span>
                      </label> 
                      <div class="custom-file-container__image-preview"></div>
                    </div>
                    <div class="custom-file-container col-6" data-upload-id="mySecondImage">
                      <label>Upload Verification Papers <a href="javascript:void(0)" class="custom-file-container__image-clear" title="Clear Image">x</a></label>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !image1 }">Please fill the image !</b-form-invalid-feedback>
                    
                      <label class="custom-file-container__custom-file">
                        <input type="file" @change="onFileChanged1" class="custom-file-container__custom-file__custom-file-input" accept="image/*" :class="[is_submit_form1 ? (image1 ? 'is-valid' : 'is-invalid') : '']" />
                        <input type="hidden" name="MAX_FILE_SIZE" value="10485760" />
                        <span class="custom-file-container__custom-file__custom-file-control"></span>
                      </label> 
                      <div class="custom-file-container__image-preview"></div>
                    </div>
                  </b-form-row>
                    <b-form-row class="mb-4">
                    <b-form-group class="col-md-12">
                      <label>Bio</label>
                      <b-textarea rows="6" cols="80" type="text" v-model="form.bio" placeholder="Entreprise details" :class="[is_submit_form1 ? (form.bio && form.bio.length<500 && form.bio.length>25 ? 'is-valid' : 'is-invalid') : '']"></b-textarea>
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.bio }">Please Enter content between 25 and 500 characters</b-form-invalid-feedback>
                    </b-form-group>
                   
                  </b-form-row>
                </b-form>
              </tab-content>
            </form-wizard>
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
import { mapGetters, mapActions } from 'vuex';
import '@/assets/sass/scrollspyNav.scss';
import { FormWizard, TabContent } from 'vue-form-wizard';
import 'vue-form-wizard/dist/vue-form-wizard.min.css';
import '@/assets/sass/forms/file-upload-with-preview.min.css';
import FileUploadWithPreview from 'file-upload-with-preview';
import '@/assets/sass/font-icons/fontawesome/css/regular.css';
import '@/assets/sass/font-icons/fontawesome/css/fontawesome.css';
export default {
  metaInfo: { title: 'User entreprise' },
  components: {
    FormWizard,
    TabContent,
  },
  data() {
    return {
      form: {
        nameE: '',
        typeE: '',
        addressE: '',
        contactE: '',
        country: '',
        bio:'',
        roleE:null,
        userE: [],
      },
      CurrentUser: [],
      is_submit_form1: false,
      ok: false,
      image: null,
      image1:null,
      roleexist:false,
    };
  },
  mounted() {
    new FileUploadWithPreview('myFirstImage', {
      images: {
        baseImage: require('@/assets/images/file-preview.png'),
        backgroundImage: '',
      },
    });
    new FileUploadWithPreview('mySecondImage', {
      images: {
        baseImage: require('@/assets/images/file-preview.png'),
        backgroundImage: '',
      },
    });
  },
  computed: {
    ...mapGetters({
      Users: 'StateUsers',
      User: 'StateUser',
      Userentreprises: 'StateUserentreprises',
      Roles:'StateRoles'
      
    }),
  },
  methods: {
    ...mapActions(['CreateRole', 'GetUsers','GetRoles', 'CreateUserentreprise', 'GetUserentreprises']),
    //upload image
    onFileChanged(event) {
      this.image = event.target.files[0];
    },
    onFileChanged1(event1) {
      this.image1 = event1.target.files[0];
    },
    onComplete: async function () {
      for (let u in this.Users) {
        if (this.Users[u].username == this.User) {
          this.form.userE = this.Users[u];
        }
      }
      this.is_submit_form1 = true;
      if (this.form.nameE && this.form.typeE && this.form.country && this.form.contactE && this.image && this.image1 && this.form.bio.length<500 && this.form.bio.length>25) {
        for (let r in this.Roles) {
            if (this.Roles[r].userRole == this.form.userE.id) {
              this.form.roleE = this.Roles[r].id;
            }
          }
        var formdata = new FormData();
          formdata.append('imageE', this.image);
          formdata.append('imageVerif', this.image1);
        formdata.append('typeE', this.form.typeE);
        formdata.append('nameE', this.form.nameE);
        formdata.append('addressE', this.form.addressE);
        formdata.append('contactE', this.form.contactE);
        if (this.form.roleE != null) {
          formdata.append('roleE', this.form.roleE);
        }
        formdata.append('country', this.form.country);
        formdata.append('bio', this.form.bio);
        formdata.append('userE', this.form.userE.id);
        //
          this.CreateUserentreprise(formdata);
          this.$swal('Good Job!', 'Your entreprise has been created successfuly, Please wait for the administrator to publish it !', 'success');
          this.$router.push('/')
        return true;
      } else {
        return false;
      }
    },
  },

  created() {
    this.GetUsers();
    this.GetUserentreprises();
    this.GetRoles()
    if(this.User==null){
      this.$router.push('/login');
    }
    
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
        for(let r in this.Roles){
          if (this.Roles[r].userRole==this.CurrentUser.id){
            this.roleexist=true
          }
        }
        if(this.roleexist==false){
          this.CreateRole({entreprise:true,userRole:this.CurrentUser.id})
        }
        for (let u in this.Userentreprises) {
          if (this.Userentreprises[u].userE == this.CurrentUser.id) {
            this.$router.push('/entreprises');
          }
        }
      }
    }
  },
};
</script>