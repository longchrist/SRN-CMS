<?php

class brand_model extends CI_Model{

    /**
    *   Updates users last active 
    */
    public function retrieveAllBrands(){
		$result = array();
		//$result = "";
			$this->db->select('*');
			$this->db->from('srn_brand');
			$query = $this->db->get();
			$resultQuery = $query->result();
			//$projects_count = count($query->result());
			$result[] = array("data" => $resultQuery);

		return json_encode($result);
    }
}

?>