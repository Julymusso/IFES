<?php
		
	/**
	*  conexão com o banco de dados usando mysqli
	*/


	class Db{
		
		private $con;

		// Faz a conexão com o banco assim que o objeto é criado
		function __construct(){
			$this->con = mysqli_connect('sql313.byethost7.com', 'b7_27892928', 'eu', 'b7_27892928_bancolsi2021');
			if (mysqli_connect_errno($this->con)) {
				echo "Problemas para conectar no banco. Verifique os dados!";
				die();
			}
		}

		// Faz a consulta sql
		public function query($sql){
			return mysqli_query($this->con, $sql);
		}
	}

?>