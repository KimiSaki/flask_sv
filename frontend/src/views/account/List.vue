
<template>
  <div class="account_list">
    <p>{{ message }}</p>
    <h3>アカウント一覧</h3>
    <v-simple-table>
      <template v-slot;default>
        <thead>
          <tr>
            <th>アカウントID</th>
            <th>アカウント名称</th>
            <th>有効開始日</th>
            <th>有効終了日</th>
            <th>作成者</th>
            <th>作成日時</th>
            <th>更新者</th>
            <th>更新日時</th>
            <th>ステータス</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="account in accounts" v-bind:key="account">
            <td>{{ account.id }}</td>
            <td>{{ account.account_name }}</td>
            <td>{{ account.start_on }}</td>
            <td>{{ account.end_on }}</td>
            <td>{{ account.created_by }}</td>
            <td>{{ account.created_at}} </td>
            <td>{{ account.updated_by }}</td>
            <td>{{ account.updated_at }}</td>
            <td>{{ account.status }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>
<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

var accounts = [
	{
		id: 123,
		account_name: "flask_sv_front",
		start_on: "2021/02/01 10:00:00",
		end_in: "2021/11/30 18:00:00",
		created_by: 10, 
		created_at: "2021/08/25 12:00:00",
		updated_by: 10, 
		updated_at: "2021/08/25 12:00:00",
		status: 0
	},
	{
		id: 124,
		account_name: "yamada",
		start_on: "2021/05/01 10:00:00",
		end_in: "2021/10/30 18:00:00",
		created_by: 12, 
		created_at: "2021/08/25 12:00:00",
		updated_by: 10, 
		updated_at: "2021/08/25 12:00:00",
		status: 1
	}
]

export default {
  name: "SS",
  data() {
	  return {
		  accounts: accounts
	  }
  },
};
</script>
