<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Bienvenido a Djacket
        </p>
        <p class="subtitle">
          La mejor tienda de chaquetas en línea
        </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Últimos productos</h2>
      </div>

      <div 
        class="column is-3"
        v-for="product in latestProducts"
        :key="product.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail" alt="Imagen del producto">
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts() {
      axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.error('Error al obtener los últimos productos:', error)
        })
    }
  }
}
</script>
