<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Dashboard</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Add Types</span></li>
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
                      <h4>Add Type</h4>
                    </div>
                  </div>
                </div>
                <div class="panel-body">
                  <b-form novalidate @submit.prevent="submit">
                    <label >Type name <span style="color:red">*</span></label>
                    <b-form-group class="mb-3">
                      <b-input type="text" placeholder="Type name " v-model="form.descT" :class="[is_submit_form1 ? (form.descT && form.descT.length<20 && form.descT.length>4 ? 'is-valid' : 'is-invalid') : '']"></b-input>
                      <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                      <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.descT  }">Please Enter a name between 4 and 20 characters</b-form-invalid-feedback>
                    </b-form-group>
                   
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
  metaInfo: { title: 'Add Service Types' },
  components: {
   // VueTagsInput,
    },
  data() {
    return {
      form: {
        descT: '',
      },
      image:null,
     
      is_submit_form1:false, 
    };
  },
  created: function() {
    this.GetServicetypes()
      
  },
    methods: {
  
    ...mapActions(["GetServicetypes"]),
    async submit() {
      try {
        this.is_submit_form1 = true;
                if (this.form.descT && this.form.descT.length<20 && this.form.descT.length>4 )
               
                {
        
      var formdata = new FormData();
      
        formdata.append("descT", this.form.descT);
        
        await axios.post("/servicetype/servicetype-create/", formdata);
        this.$swal('Good Job!', 'Type created successfully !', 'success');
        this.$router.push("/dashboard/typeslist");
        }
      } catch (error) {
        throw "Il ya un error!"
      }
    },
    
    },
    computed: {
    ...mapGetters({Servicetypes:"StateServicetypes"}),
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
    },
};
</script>