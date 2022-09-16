<template>
  <div class="container my-8">
    <div
      class="flex justify-center items-center h-96"
      v-if="loading"
      role="status"
    >
      <svg
        aria-hidden="true"
        class="mr-2 w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
        viewBox="0 0 100 101"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
          fill="currentColor"
        />
        <path
          d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
          fill="currentFill"
        />
      </svg>
      <span class="sr-only">Loading...</span>
    </div>
    <div v-if="item" class="grid grid-cols-12 gap-8">
        <div class="col-span-3">
            <aside class="h-screen sticky top-2">
              <h1 class="text-xl font-bold my-2">{{item.fullTitle}}</h1>
              <img :src="`https://imdb-api.com/API/ResizeImage?apiKey=k_lc0zmc7m&size=400x600&url=`+item.image" :alt="item.title">
            </aside>
        </div>
        <div class="col-span-9">
            <div class="mt-4">
              <ul class="flex gap-4">
                  <li class="px-2 bg-gray-300 rounded-lg" v-for="(genre, index) in item.genreList" :key="index"><small>{{ genre.value }}</small></li>
              </ul>
            </div>
            <div>
              <iframe :src="item.trailer.linkEmbed" frameborder="0" width="1008" height="500"></iframe>
                <!-- <iframe :src="item.trailer.linkEmbed" frameborder="0" width="100%" height="500"></iframe> -->
            </div>
            <div>
              <ul class="flex gap-8">
                <li>IMDB<Icon icon="la:imdb" color="#ffc107" width="45" />{{ item.ratings.imDb }}</li>
                <li>metacritic<Icon icon="emojione:film-frames" color="#ffc107" width="45" />{{ item.ratings.metacritic }}</li>
                <li>theMovieDb<Icon icon="fontisto:film" color="#ffc107" width="45" />{{ item.ratings.theMovieDb }}</li>
                <li>rottenTomatoes<Icon icon="simple-icons:rottentomatoes" color="#ffc107" width="45" />{{ item.ratings.rottenTomatoes }}</li>
                <li>filmAffinity<Icon icon="fluent-emoji-high-contrast:film-projector" color="#ffc107" width="45" />{{ item.ratings.filmAffinity }}</li>
              </ul>
            </div>
            
            <div class="grid grid-cols-12">
              <div class="col-span-8">
                <ul class="grid grid-cols-2 justify-between">
                  <li class=" mb-4" v-for="(actor, index) in item.actorList.slice(0, 10)" :key="index">
                      <div><img class="rounded-full mt-4 w-[150px] h-[150px]" :src="`https://imdb-api.com/API/ResizeImage?apiKey=k_lc0zmc7m&size=150x150&url=`+actor.image" :alt="actor.name"></div>
                      <h3><router-link :to="{name: 'actor', params:{id: actor.id}}">{{ actor.name }}</router-link></h3>
                      <p class="text-gray-400">{{ actor.asCharacter }}</p>
                  </li>
                </ul>
              </div>
              <div class="col-span-4">
                <ul class="bg-blue-50 p-4 sticky h-screen top-2">
                  <li>
                    <h4>Director:</h4>
                    <p>{{ item.directorList[0].name }}</p>
                  </li>
                  <li>
                    <h4>writers:</h4>
                    <p>{{ item.writers }}</p>
                  </li>
                  <li>
                    <h4>country</h4>
                    <template v-for="(country, index) in item.countryList" :key="index">
                      <p>{{ country.value }}</p>
                    </template>
                  </li>
                  <li>
                    <h4>Language: </h4>
                    <p>{{ item.languages }}</p>
                  </li>
                  <li>
                    <h4>stars:</h4>
                    <p>{{ item.stars }}</p>
                  </li>
                  <li>
                    <h4>Genres:</h4>
                    <p>{{ item.genres }}</p>
                  </li>
                  <li>
                    <h4>Release Date:</h4>
                    <p>{{ item.releaseDate }}</p>
                  </li>
                  <li>
                    <h4>Run Time:</h4>
                    <p>{{ item.runtimeStr }}</p>
                  </li>
                </ul>
              </div>
            </div>
        </div>
    </div>

    <div class=" mt-8">
        <h4 class="text-2xl mb-2">Similars</h4>
        <ul class="md:grid md:grid-cols-6 grid-cols-2 gap-4">
            <li v-for="(similar, index) in item.similars" :key="index" class="bg-blue-50 border border-blue-100 rounded-md flex flex-col gap-2 justify-center px-5 py-4">
                <router-link :to="{name: 'single', params:{id:similar.id}}">{{ similar.title }}</router-link>
                <img :src="`https://imdb-api.com/API/ResizeImage?apiKey=k_lc0zmc7m&size=250x400&url=`+similar.image" :alt="similar.title">
                <div class="">
                  <small>IMDb Rating: {{ similar.imDbRating }}</small>
                </div>
            </li>
        </ul>
    </div>


  </div>
</template>

<script setup lang="ts">
    import { Icon } from '@iconify/vue';
    import { ref } from "@vue/reactivity";
    import axios from "axios";
    import { useRoute } from "vue-router";
    const item:any = ref([]);
    const loading = ref(true);
    const route = useRoute();
    
    function getSingle() {
      axios
        .get(
          `https://imdb-api.com/en/API/Title/k_lc0zmc7m/${route.params.id}/FullActor,FullCast,Posters,Images,Trailer,Ratings,Wikipedia`
        )
        .then(function (response) {
          item.value = response.data;
          loading.value = false;
        })
        .catch(function (error) {
          console.log(error);
        });
    }
    getSingle();

    
</script>

    

<style scoped>
.video-player-frame {
  width: 100% !important;
}

</style>