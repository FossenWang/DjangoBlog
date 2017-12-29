
function addTrainingDay(){
    var program_pk = parseInt($("#program_pk").text());
    var vtf = parseInt($("#id_day-TOTAL_FORMS").val());
    if (!vtf){ vtf=0 }
    var newTD = '<div class="training-day">'+
        '<div class="title">'+
        '<span>天数: </span>'+
        '<input type="number" name="day-'+vtf+'-day" value='+(vtf+1)+' min="0" id="id_day-'+vtf+'-day">'+
        '<span>名称: </span>'+
        '<input type="text" name="day-'+vtf+'-name" value="练背日" maxlength="16" id="id_day-'+vtf+'-name">'+
        '<span>删除: </span>'+
        '<button type="button" class="delete-sets">×</button>'+
        '<input type="hidden" name="day-'+vtf+'-program" value='+program_pk+' id="id_day-'+vtf+'-program">'+
        '<table><tbody>'+
        '<input type="hidden" name="day-'+vtf+'-sets-TOTAL_FORMS" value="0" id="id_day-'+vtf+'-sets-TOTAL_FORMS">'+
        '<input type="hidden" name="day-'+vtf+'-sets-INITIAL_FORMS" value="0" id="id_day-'+vtf+'-sets-INITIAL_FORMS">'+
        '<input type="hidden" name="day-'+vtf+'-sets-MIN_NUM_FORMS" value="0" id="id_day-'+vtf+'-sets-MIN_NUM_FORMS">'+
        '<input type="hidden" name="day-'+vtf+'-sets-MAX_NUM_FORMS" value="1000" id="id_day-'+vtf+'-sets-MAX_NUM_FORMS">'+
        '<tr><td class="col1">动作</td><td class="col1">RM</td><td class="col2">组数</td><td class="col2">休息/s</td><td class="col2">删除</td></tr>'+
        '<tr class="addsets" id="id_day-'+vtf+'-addsets">'+
        '<td colspan="5">＋新增一组动作</td></tr></tbody></table></div>';
    $("#id_day-TOTAL_FORMS").val(vtf+1);
    $(".add-training-day").parent().before(newTD);
    $("#id_day-"+vtf+"-addsets").click(addSets);
}

function addSets(){
	var id_addsets = $(this).attr("id");
	var day_id = parseInt($("#"+id_addsets.replace("addsets","id")).val());
	var id_total_forms = id_addsets.replace("addsets", "sets-TOTAL_FORMS");
	var vtf = parseInt($("#"+id_total_forms).val());
	var id_prefix = id_addsets.replace("addsets", "sets-"+vtf);
	var name_prefix = id_prefix.replace("id_","");
    var newSets = '<tr>'+
    	'<td class="col1" title="备选动作: 哑铃卧推">哑铃卧推</td>'+
		'<td class="col1">'+
	    '<input type="number" name="'+name_prefix+'-minreps" value="8" min="0" id="'+id_prefix+'-minreps" >'+
		'~<input type="number" name="'+name_prefix+'-maxreps" value="12" min="0" id="'+id_prefix+'-maxreps" >'+
		'</td><td class="col2"><input type="number" name="'+name_prefix+'-sets" value="5" min="0" id="'+id_prefix+'-sets" ></td>'+
		'<td class="col2"><input type="number" name="'+name_prefix+'-rest" value="120" min="0" id="'+id_prefix+'-rest" ></td>'+
		'<td class="col2">'+
	    '<button type="button" class="delete-sets">×</button>'+
		'<input type="hidden" name="'+name_prefix+'-trainingday" value='+day_id+' id="'+id_prefix+'-trainingday" >'+
		'<input type="hidden" name="'+name_prefix+'-number" value='+(vtf+1)+' id="'+id_prefix+'-number" ></td></tr>';
	$("#"+id_total_forms).val(vtf+1);
	$("#"+id_addsets).before(newSets);
	$("#"+id_prefix+"-number").parent().children(".delete-sets").click(deleteNewSets);
}

function deleteOldForm(){
	$(this).siblings("input[name$='DELETE']").attr("checked", true);
	$(this).parent().parent().hide();
}

function deleteNewSets(){
	var id_total_forms = $(this).next().attr("id").split("sets")[0] + "sets-TOTAL_FORMS";
	var vtf = parseInt($("#"+id_total_forms).val());
	$("#"+id_total_forms).val(vtf-1);
	var this_sets = $(this).parent().parent();
	var next_sets = this_sets.nextUntil(".addsets");
	if (next_sets.length>0){
		copySetsValue(this_sets, next_sets.eq(0));
		for (var i=1; i<next_sets.length; i++ ){
			copySetsValue(next_sets.eq(i-1), next_sets.eq(i));
		}
		next_sets.last().remove();
	}else{
		this_sets.remove();
	}
}

function copySetsValue(sets1, sets2){
	var inputs1 = sets1.find("input");
	var inputs2 = sets2.find("input");
	for (var i=0; i<inputs1.length; i++){
		inputs1.eq(i).val(inputs2.eq(i).val());
	}
}