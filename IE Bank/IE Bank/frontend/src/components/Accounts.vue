<template>

  <h1
    class="bg-gradient-to-r from-green-300 via-blue-500 to-purple-600 bg-clip-text text-3xl font-extrabold text-transparent sm:text-5xl text-center my-20">
    Table of users
  </h1>
    <div class="overflow-x-auto flex justify-center">
      <table class="min-w-[80dvw] divide-y-2 divide-white bg-gray-900 text-sm">
        <thead class="ltr:text-left rtl:text-right">
          <tr>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-white">ID</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-white">Nombre</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-white">Email</th>
            <th class="whitespace-nowrap px-4 py-2 font-medium text-white">Saldo</th>
          </tr>
        </thead>
    
        <tbody class="divide-y divide-gray-200">
          <tr v-for="cuenta in cuentas" :key="cuenta.id">
            <td class="whitespace-nowrap px-4 py-2 font-medium text-white">{{ cuenta.id }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-white">{{ cuenta.nombre }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-white">{{ cuenta.email }}</td>
            <td class="whitespace-nowrap px-4 py-2 text-white">{{ cuenta.saldo }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        cuentas: [
          { id: 1, nombre: 'Juan Pérez', email: 'juan@example.com', saldo: 1000.0 },
          { id: 2, nombre: 'María García', email: 'maria@example.com', saldo: 500.0 },
          { id: 3, nombre: 'Pedro López', email: 'pedro@example.com', saldo: 2000.0 }
        ]
      }
    },
    mounted() {
      this.fetchCuentas()
    },
    methods: {
      fetchCuentas() {
        fetch('/accounts')
      .then(response => response.json())
      .then(data => {
            if (data.cuentas.length > 0) {
              this.cuentas = data.cuentas
            }
          })
      .catch(error => console.error(error))
      }
    }
  }
  </script>
  