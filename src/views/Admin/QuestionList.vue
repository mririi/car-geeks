<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Dashboard</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Questions</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    
                <div id="tableHover" class="col-lg-12 col-12 layout-spacing mt-5">
                    <div class="statbox panel box box-shadow">
                        
                        <div class="panel-body">
                            <b-table
                                responsive
                                bordered
                                hover
                                :items="Questions"
                                :fields="['Title', 'Details', 'Date','Category','Replies number','User', { key: 'status', label: 'status', class: 'text-center' }]"
                            >
                                <template #cell(status)="row">
                                    <span
                                        :class="{
                                            'text-success': row.value == 'Complete',
                                            'text-secondary': row.value == 'Pending',
                                            'text-info': row.value == 'In progress',
                                            'text-danger': row.value == 'Canceled'
                                        }"
                                    >
                                        {{ row.value }}
                                    </span>
                                </template>
                               
                            </b-table>

                          
                        </div>
                    </div>
                </div>
  </div>
</template>
<style>
.table3 .actions svg {
  padding: 2px;
}
</style>
<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  metaInfo: { title: 'Bootstrap Custom Table' },
  data() {
    return {
    
      category: [],
      CurrentUserProfile: [],
      CurrentUser: [],
    };
  },
 
 
  methods: {
      ...mapActions(['GetQuestions', 'GetUsers', 'GetUserprofiles', 'GetQuestioncategories']),
   
  },
  computed: {
    ...mapGetters({
      Questions: 'StateQuestions',
      Userprofiles: 'StateUserprofiles',
      Questioncategories: 'StateQuestioncategories',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
  },
  created: function () {
    this.GetQuestions();
    this.GetUserprofiles();
    this.GetQuestioncategories();
    this.GetUsers();
    for (let u in this.Users) {
      if (this.Users[u].username == this.User) {
        this.CurrentUser = this.Users[u];
      }
    }
    for (let u in this.Userprofiles) {
      if (this.Userprofiles[u].userU == this.CurrentUser.id) {
        this.CurrentUserProfile = this.Userprofiles[u];
      }
    }
  },
};
</script>
