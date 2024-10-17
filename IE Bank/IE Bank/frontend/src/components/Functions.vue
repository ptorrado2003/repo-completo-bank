
<script>
export default {
  data() {
    return {
      mode: '',
      form: {
        nombre: '',
        email: '',
        saldo: 0
      }
    }
  },
  methods: {
    openDialog(mode) {
      this.mode = mode
      this.$refs.dialog.showModal()
    },
    closeDialog() {
      this.$refs.dialog.close()
    },
    handleSubmit() {
      if (this.mode === 'create') {
        fetch('http://localhost:5000/accounts', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        })
     .then(response => response.json())
     .then(data => console.log(data))
     .catch(error => console.error(error))
      } else if (this.mode === 'edit') {
        fetch('http://localhost:5000/accounts', {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        })
     .then(response => response.json())
     .then(data => console.log(data))
     .catch(error => console.error(error))
      } else if (this.mode === 'delete') {
        fetch('http://localhost:5000/accounts', {
          method: 'DELETE',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        })
     .then(response => response.json())
     .then(data => console.log(data))
     .catch(error => console.error(error))
      }
      this.closeDialog()
    }
  }
}
</script>


<template>
    <div>

      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" @click="openDialog('create')">Crear cuenta</button>
      <button class="bg-orange-500 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded" @click="openDialog('edit')">Editar cuenta</button>
      <button class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded" @click="openDialog('delete')">Eliminar cuenta</button>
  
      <dialog class="bg-gray-800 text-white p-12" id="dialog" ref="dialog">
  <form @submit.prevent="handleSubmit">
    <h2 v-if="mode === 'create'">Crear cuenta</h2>
    <h2 v-if="mode === 'edit'">Editar cuenta</h2>
    <h2 v-if="mode === 'delete'">Eliminar cuenta</h2>
    <div v-if="mode!== 'delete'">
      <label
        for="nombre"
        class="relative block overflow-hidden border-b border-gray-200 bg-transparent pt-3 focus-within:border-blue-600"
      >
        <input
          type="text"
          id="nombre"
          placeholder="Nombre"
          v-model="form.nombre"
          class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm"
        />
        <span
          class="absolute start-0 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs"
        >
          Nombre
        </span>
      </label>
      <label
        for="email"
        class="relative block overflow-hidden border-b border-gray-200 bg-transparent pt-3 focus-within:border-blue-600"
      >
        <input
          type="email"
          id="email"
          placeholder="Email"
          v-model="form.email"
          class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm"
        />
        <span
          class="absolute start-0 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs"
        >
          Email
        </span>
      </label>
      <label
        for="saldo"
        class="relative block overflow-hidden border-b border-gray-200 bg-transparent pt-3 focus-within:border-blue-600"
      >
        <input
          type="number"
          id="saldo"
          placeholder="Saldo"
          v-model="form.saldo"
          class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm"
        />
        <span
          class="absolute start-0 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs"
        >
          Saldo
        </span>
      </label>
    </div>
    <div v-if="mode === 'delete'">
    <label
      for="nombreEliminar"
      class="relative block overflow-hidden border-b border-gray-200 bg-transparent pt-3 focus-within:border-blue-600"
    >
      <input
        type="text"
        id="nombreEliminar"
        placeholder="Nombre de la cuenta a eliminar"
        v-model="nombreEliminar"
        class="peer h-8 w-full border-none bg-transparent p-0 placeholder-transparent focus:border-transparent focus:outline-none focus:ring-0 sm:text-sm"
      />
      <span
        class="absolute start-0 top-2 -translate-y-1/2 text-xs text-gray-700 transition-all peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-sm peer-focus:top-2 peer-focus:text-xs"
      >
        Nombre de la cuenta a eliminar
      </span>
    </label>
    <p>¿Estás seguro de que deseas eliminar la cuenta?</p>
  </div>
    <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" type="submit">Enviar</button>
    <button class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded" type="button" @click="closeDialog">Cancelar</button>
  </form>
</dialog>

    </div>
  </template>
  