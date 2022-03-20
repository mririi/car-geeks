<template>
  <div class="relative overflow">
    
                      
    <search-focus @keyup="focusSearch" />
    <div class="relative w-80">
      
      <input
        type="text"
        placeholder="Search (Press  &quot;/&quot; to focus)"
        class="col-lg-8 col-md-8 col-sm-9 filtered-list-search-live mx-auto w-100 product-search br-30 mt-3"
        v-model="query"
        @blur="searchResultsVisible = false"
        @focus="searchResultsVisible = true"
        @keydown.esc="searchResultsVisible = false"
        @input="softReset"
        ref="search"
        @keyup="performSearch"
        @keydown.up.prevent="highlightPrevious"
        @keydown.down.prevent="highlightNext"
        @keydown.enter="gotoLink"
      >
      <div class="absolute top-0 ml-3" style="top:10px">
       
      </div>
      <div
        v-if="query.length > 0"
        class="absolute top-0 right-0 text-2xl mr-3 cursor-pointer text-gray-600 hover:text-gray-800"
        style="top:2px;"
        @click="reset"
      >
        &times;
      </div>
    </div>
    <transition name="fade">
      <div v-if="query.length > 0 && searchResultsVisible" class="absolute normal-case bg-white border left-0 right-0 w-108 text-left mb-4 mt-2 rounded-lg shadow overflow-hidden z-10 overflow-y-auto" style="max-height: 32rem">
        <div class="flex flex-col" ref="results">
          <a
            v-for="(question, index) in searchResults"
            :key="index"
            href="question.item.path"
            @mousedown.prevent="searchResultsVisible = true"
            class="border-b border-gray-700 text-xl cursor-pointer p-4 hover:bg-blue-700"
           
            :class="{ 'bg-blue-700': index === highlightedIndex }"
          >
            {{ question.item.titleQ }}

            
          </a>

          <div v-if="searchResults.length === 0" class="font-normal w-full border-b cursor-pointer p-4">
            <p class="my-0">No results for '<strong>{{ query }}</strong>'</p>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import SearchFocus from './SearchFocus'
import { mapGetters, mapActions } from "vuex";

export default {
  components: {
    SearchFocus,
  },
  data() {
    return {
      query: '',
      searchResultsVisible: false,
      searchResults: [],
      highlightedIndex: 0,
      options: {
        shouldSort: true,
        includeMatches: true,
        threshold: 0.5,
        location: 0,
        distance: 500,
        maxPatternLength: 32,
        minMatchCharLength: 1,
        keys: ['titleQ', 'contentQ']
      }
    }
  },
  created() {
    this.GetQuestions()
  },
  computed: {
            ...mapGetters({
            Questions: "StateQuestions",
            }),
        },
  methods: {
     ...mapActions([
      "GetQuestions"
    ]),
    reset() {
      this.query = ''
      this.highlightedIndex = 0
    },
    softReset() {
      this.searchResultsVisible = true
      this.highlightedIndex = 0
    },
    focusSearch(e) {
      if (e.key === '/') {
        this.$refs.search.focus()
      }
    },
    performSearch() {
      this.$search(this.query, this.Questions, this.options)
        .then(results => {
          this.searchResults = results
        })
    },
    highlightPrevious() {
      if (this.highlightedIndex > 0) {
        this.highlightedIndex = this.highlightedIndex - 1
        this.scrollIntoView()
      }
    },
    highlightNext() {
      if (this.highlightedIndex < this.searchResults.length - 1) {
        this.highlightedIndex = this.highlightedIndex + 1
        this.scrollIntoView()
      }
    },
    scrollIntoView() {
      this.$refs.results.children[this.highlightedIndex].scrollIntoView({ block: 'nearest' })
    },
    gotoLink() {
      if (this.searchResults[this.highlightedIndex]) {
        window.location = this.searchResults[this.highlightedIndex].item.path
      }
    }
  }
}
</script>

<style scoped>
 /* .fade-enter-active, .fade-leave-active {
    transition: opacity .2s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }*/
</style>

