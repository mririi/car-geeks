<template>
  <div class="layout-px-spacing">
    <portal to="breadcrumb">
      <ul class="navbar-nav flex-row">
        <li>
          <div class="page-header">
            <nav class="breadcrumb-one" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="javascript:;">Dashboard</a></li>
                <li class="breadcrumb-item active" aria-current="page"><span>Post Request</span></li>
              </ol>
            </nav>
          </div>
        </li>
      </ul>
    </portal>

    <div class="row layout-top-spacing">
      <div class="col-xl-12 col-lg-12 col-sm-12 layout-spacing">
        <div class="panel p-0">
          <div class="custom-table table3">
            <div class="table-header">
              <div class="d-flex align-items-center">
                <span>Results :</span>
                <span class="ml-2">
                  <b-select v-model="table_option2.page_size" class="h-auto">
                    <b-select-option value="5">5</b-select-option>
                    <b-select-option value="10">10</b-select-option>
                    <b-select-option value="20">20</b-select-option>
                    <b-select-option value="50">50</b-select-option>
                  </b-select>
                </span>
              </div>

              <div class="header-search">
                <b-input v-model="search" size="sm" placeholder="Search..." />

                <div class="search-image">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="feather feather-search"
                  >
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                  </svg>
                </div>
              </div>
            </div>

            <b-table
              ref="basic_table2"
              responsive
              hover
              bordered
              :items="filteredList"
              :fields="columns2"
              :per-page="table_option2.page_size"
              :current-page="table_option2.current_page"
              :filter="table_option2.search_text"
              sort-by="id"
              :show-empty="true"
              @filtered="on_filtered"
              @sort-changed="clear_selection"
            >
              <template #cell(accepted)>
                <span>
                  <b-badge variant="danger">Pending</b-badge>
                </span>
              </template>
                <template #cell(userprofilePost)="data">
              <span v-if="data.item.userprofilePost!=null">
              <span v-for="u in Userprofiles" :key="u.id">
                <span v-if="u.id == data.item.userprofilePost">
                  <router-link :to="'/profile/'+data.item.userprofilePost">
                   {{ u.firstname }} {{ u.lastname }} 
                  </router-link>
                   </span>
                </span></span>
                <span v-if="data.item.userentreprisePost!=null">
                <span v-for="e in Userentreprises" :key="e.id">
                <span v-if="e.id == data.item.userentreprisePost">
                  <router-link :to="'/entreprisedetails/'+data.item.userentreprisePost">
                   {{ e.nameE }} 
                  </router-link>
                   </span>
              </span></span>
            </template>
              <template #cell(actions)="data">
                <span @click="Accept(data.item)">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="feather feather-check-circle text-primary ac"
                  >
                    <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                    <polyline points="22 4 12 14.01 9 11.01"></polyline>
                  </svg>
                </span>
              </template>
              <template #cell(imagePost)="data">
                <span v-if="data.item.imagePost != null">
                  <b-avatar :src="'http://127.0.0.1:8000' + data.item.imagePost" size="4rem" rounded="lg" alt="" srcset="" />
                </span>
                <span v-else>
                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="4em" height="4em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 64 64">
                    <path
                      fill="currentColor"
                      d="M32 2C15.432 2 2 15.432 2 32.001C2 48.567 15.432 62 32 62s30-13.433 30-29.999C62 15.432 48.568 2 32 2zm22 30.001c0 4.629-1.433 8.922-3.876 12.465l-30.591-30.59A21.889 21.889 0 0 1 32 10c12.15 0 22 9.851 22 22.001zm-44 0a21.9 21.9 0 0 1 3.876-12.468l30.591 30.591A21.887 21.887 0 0 1 32 54.001c-12.15 0-22-9.852-22-22z"
                    />
                  </svg>
                </span>
              </template>
            </b-table>

            <div class="table-footer">
              <div class="dataTables_info">Showing {{ meta2.total_items ? meta2.start_index + 1 : 0 }} to {{ meta2.end_index + 1 }} of {{ meta2.total_items }}</div>
              <div class="paginating-container pagination-solid flex-column align-items-right">
                <b-pagination
                  v-model="table_option2.current_page"
                  :total-rows="table_option2.total_rows"
                  :per-page="table_option2.page_size"
                  prev-text="Prev"
                  next-text="Next"
                  first-text="First"
                  last-text="Last"
                  first-class="first"
                  prev-class="prev"
                  next-class="next"
                  last-class="last"
                  class="rounded"
                >
                  <template #first-text>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 19l-7-7 7-7m8 14l-7-7 7-7" />
                    </svg>
                  </template>
                  <template #prev-text>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                    </svg>
                  </template>
                  <template #next-text>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                    </svg>
                  </template>
                  <template #last-text>
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7" />
                    </svg>
                  </template>
                </b-pagination>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.table3 .actions svg {
  padding: 2px;
}
.ac {
  cursor: pointer;
}
</style>
<script>
import { mapGetters, mapActions } from 'vuex';
import axios from 'axios';
export default {
  metaInfo: { title: 'Posts Requests' },
  data() {
    return {
      //table 3
      items2: [],
      columns2: [],
      table_option2: { total_rows: 0, current_page: 1, page_size: 5, search_text: '' },
      meta2: {},
      is_select_all2: false,
      selected_rows2: [],
      search: '',
      category: '',
      group: [],
      pendingmember: [],
      pendingUserprofiles: [],
    };
  },
  watch: {
    table_option: {
      handler: function () {
        this.get_meta();
        this.clear_selection();
      },
      deep: true,
    },
    table_option1: {
      handler: function () {
        this.get_meta1();
        this.clear_selection1();
      },
      deep: true,
    },
    table_option2: {
      handler: function () {
        this.get_meta2();
        this.clear_selection2();
      },
      deep: true,
    },
  },
  created: function () {
    this.GetGroups();
    this.GetGroupposts();
    this.GetUserprofiles();
    this.GetGroupcomments();
    this.GetGroupmembers();
    this.GetUserentreprises();
    this.GetUsers();
    axios.get('/group/group-detail/' + this.$route.params.id + '/').then((response) => {
      this.group = response.data;

      for (let m in this.Members) {
        if (this.Members[m].groupMem == this.group.id && this.Members[m].accepted == false) {
          this.pendingmember.push(this.Members[m]);
        }
      }

      let i = 0;
      for (let up in this.Userprofiles) {
        for (i in this.pendingmember)
          if (this.Userprofiles[up].id == this.pendingmember[i].userprofileMem) {
            this.pendingUserprofiles.push(this.Userprofiles[up]);
            i++;
          }
      }
    });
  },
  mounted() {
    this.bind_data();
  },

  computed: {
    ...mapGetters({
      Groups: 'StateGroups',
      GroupPost: 'StateGroupposts',
      Userprofiles: 'StateUserprofiles',
      Userentreprises:'StateUserentreprises',
      Comments: 'StateGroupcomments',
      Members: 'StateGroupmembers',
      User: 'StateUser',
      Users: 'StateUsers',
    }),
    filteredList() {
      return this.GroupPost.filter((post) => {
        return  post.accepted == false;
      });
    },
  },

  methods: {
    ...mapActions(['GetGroups','GetUserentreprises' ,'GetGroupposts', 'GetUsers', 'GetUserprofiles', 'GetGroupcomments', 'GetGroupmembers', 'CreateGroupmember']),
    async Accept(post) {
      this.$swal({
        icon: 'warning',
        title: 'Are you sure?',
        showCancelButton: true,
        confirmButtonText: 'Accept',
        padding: '2em',
      }).then((result) => {
        if (result.value) {
          axios.put('/postgroup/postgroup-update/' + post.id + '/', { accepted: true });

          axios.put('/group/group-update/' + this.$route.params.id + '/', { nbposts: this.group.nbposts + 1 });
          this.$router.go();
          this.$swal('Accepted!', 'Post has been added to your group.', 'success');
        }
      });
    },
    bind_data() {
      //table 3
      (this.columns2 = [
        { key: 'imagePost', label: 'Image', class: 'text-center  ' },
        { key: 'detailsP', label: 'Details' },
        { key: 'userprofilePost', label: 'User' },
        { key: 'accepted', label: 'Status', class: 'text-center  ' },
        { key: 'actions', label: 'Actions', class: 'text-center  ' },
      ]),
        (this.table_option2.total_rows = this.filteredList.length);
      this.get_meta2();
    },
    on_filtered(filtered_items) {
      this.refresh_table(filtered_items.length);
    },
    refresh_table(total) {
      this.table_option.total_rows = total;
      this.table_option.currentPage = 1;
    },
    get_meta() {
      this.meta = this.get_common_meta(this.table_option);
    },

    get_common_meta(table_option) {
      var startPage;
      var endPage;
      var totalPages = table_option.page_size < 1 ? 1 : Math.ceil(table_option.total_rows / table_option.page_size);
      totalPages = Math.max(totalPages || 0, 1);

      var maxSize = 5;
      var isMaxSized = typeof maxSize !== 'undefined' && maxSize < totalPages;
      if (isMaxSized) {
        startPage = Math.max(table_option.current_page - Math.floor(maxSize / 2), 1);
        endPage = startPage + maxSize - 1;

        if (endPage > totalPages) {
          endPage = totalPages;
          startPage = endPage - maxSize + 1;
        }
      } else {
        startPage = 1;
        endPage = totalPages;
      }
      let startIndex = (table_option.current_page - 1) * table_option.page_size;
      let endIndex = Math.min(startIndex + table_option.page_size - 1, table_option.total_rows - 1);

      var pages = Array.from(Array(endPage + 1 - startPage).keys()).map((i) => startPage + i);
      return {
        total_items: table_option.total_rows,
        current_page: table_option.current_page,
        page_size: table_option.page_size,
        total_pages: totalPages,
        start_page: startPage,
        end_page: endPage,
        start_index: startIndex,
        end_index: endIndex,
        pages: pages,
      };
    },

    //checkbox selection
    select_all() {
      this.selected_rows = this.$refs.basic_table.paginatedItems.map((d) => {
        return d.id;
      });
      if (!this.is_select_all) {
        this.clear_selection();
      }
      this.check_select_all();
    },
    check_select_all() {
      let ids = this.$refs.basic_table.paginatedItems.map((d) => {
        return d.id;
      });
      this.is_select_all = false;
      if (ids.length == this.selected_rows.length) {
        this.is_select_all = true;
      }
    },
    clear_selection() {
      this.is_select_all = false;
      this.selected_rows = [];
    },

    //table 2
    on_filtered1(filtered_items) {
      this.refresh_table1(filtered_items.length);
    },
    refresh_table1(total) {
      this.table_option1.total_rows = total;
      this.table_option1.currentPage = 1;
    },
    get_meta1() {
      this.meta1 = this.get_common_meta(this.table_option1);
    },
    //checkbox selection
    select_all1() {
      this.selected_rows1 = this.$refs.basic_table1.paginatedItems.map((d) => {
        return d.id;
      });
      if (!this.is_select_all1) {
        this.clear_selection1();
      }
      this.check_select_all1();
    },
    check_select_all1() {
      let ids = this.$refs.basic_table1.paginatedItems.map((d) => {
        return d.id;
      });
      this.is_select_all1 = false;
      if (ids.length == this.selected_rows1.length) {
        this.is_select_all1 = true;
      }
    },
    clear_selection1() {
      this.is_select_all1 = false;
      this.selected_rows1 = [];
    },

    //table 3
    on_filtered2(filtered_items) {
      this.refresh_table2(filtered_items.length);
    },
    refresh_table2(total) {
      this.table_option2.total_rows = total;
      this.table_option2.currentPage = 1;
    },
    get_meta2() {
      this.meta2 = this.get_common_meta(this.table_option2);
    },
    //checkbox selection
    select_all2() {
      this.selected_rows2 = this.$refs.basic_table2.paginatedItems.map((d) => {
        return d.id;
      });
      if (!this.is_select_all2) {
        this.clear_selection2();
      }
      this.check_select_all2();
    },
    check_select_all2() {
      let ids = this.$refs.basic_table2.paginatedItems.map((d) => {
        return d.id;
      });
      this.is_select_all2 = false;
      if (ids.length == this.selected_rows2.length) {
        this.is_select_all2 = true;
      }
    },
    clear_selection2() {
      this.is_select_all2 = false;
      this.selected_rows2 = [];
    },
  },
};
</script>
