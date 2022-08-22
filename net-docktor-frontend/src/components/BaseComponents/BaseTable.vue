<template>
  <div>
    <table>
    <thead class="table__header">
      <th v-for="(header, headerIndex) in headers"
          :key="headerIndex"
      >
        {{header}}
      </th>
    </thead>
    <tbody>
      <tr v-for="(item, itemIndex) in items"
          :key="itemIndex"
      >
        <td>
          <span class="link">
            {{item.cs_id}}
          </span>
        </td>
        <td>{{item.customer}}</td>
        <td>{{item.name}}</td>
        <td>{{item.start}}</td>
        <td>{{item.end}}</td>
        <td>{{item.status}}</td>
      </tr>
    </tbody>
</table>
  </div>
</template>

<script>

  export default {
    components: {
    },
    props: {
      headers: {
        required: true,
        type: Array
      },
      items: {
        required: true,
        type: Array
      },
    },
    data() {
      return {
        value: null,
      }
    }
  }
</script>

<style scoped>

.table__header{
  height: 60px;
  padding: 12px 16px 12px 753px;
  background-color: #f4f6f8;
  border: solid 1px #d8d8d8;
}

th{
  font-size: 16px;
  text-align: left;
  padding: 1rem;
  font-weight: bold;
  color: #444;
  letter-spacing: 0.57px;
}

td{
  padding: 1rem;
  border: solid 1px #d8d8d8;
  font-size: 16px;
}

table{
  border-collapse: collapse;
  width: 100%;
  height: 100%;
}

.link{
  color: #00bef7 !important;
  cursor:pointer;
  text-decoration:underline;
}

.link:hover {
     text-decoration:none;
     color: #00b7f9
}
</style>