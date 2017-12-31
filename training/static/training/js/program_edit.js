
function addTrainingDay(){
    var program_pk = parseInt($("#program_pk").text());
    var vtf = parseInt($("#id_day-TOTAL_FORMS").val());
    if (!vtf){ vtf=0; }
    var number = parseInt($(this).parent().prev().find("input[name$='day']").val())+1;
    if (!number){ number = 1; }
    var newTD = '<div class="training-day">'+
        '<div class="title">'+
        '<span>第</span><span id="id_day-'+vtf+'-day-value">'+ number +'</span><span>天</span>'+
        '<input type="hidden" name="day-'+vtf+'-day" value='+number+' id="id_day-'+vtf+'-day">'+
        '<input type="text" name="day-'+vtf+'-name" value="休息日" maxlength="16" id="id_day-'+vtf+'-name">'+
        '<span>删除: </span>'+
        '<button type="button" class="delete-day">×</button>'+
        '<input type="hidden" name="day-'+vtf+'-program" value='+program_pk+' id="id_day-'+vtf+'-program"></div>'+
        '<table><tbody>'+
        '<input type="hidden" name="day-'+vtf+'-sets-TOTAL_FORMS" value="0" id="id_day-'+vtf+'-sets-TOTAL_FORMS">'+
        '<input type="hidden" name="day-'+vtf+'-sets-INITIAL_FORMS" value="0" id="id_day-'+vtf+'-sets-INITIAL_FORMS">'+
        '<input type="hidden" name="day-'+vtf+'-sets-MIN_NUM_FORMS" value="0" id="id_day-'+vtf+'-sets-MIN_NUM_FORMS">'+
        '<input type="hidden" name="day-'+vtf+'-sets-MAX_NUM_FORMS" value="1000" id="id_day-'+vtf+'-sets-MAX_NUM_FORMS">'+
        '<tr><td class="col1">动作</td><td class="col1">RM</td><td class="col2">组数</td><td class="col2">休息/s</td><td class="col2">删除</td></tr>'+
        '<tr class="addsets">'+
        '<td colspan="5">＋新增一组动作</td></tr></tbody></table>';
    $("#id_day-TOTAL_FORMS").val(vtf+1);
    $(".add-training-day").parent().before(newTD);
    $("#id_day-"+vtf+"-program").parent().parent().find(".addsets").click(addSets);
    $("#id_day-"+vtf+"-program").siblings(".delete-day").click(deleteNewDay);
}

function deleteOldDay(){
	var this_day = $(this).parent().parent();
    var next_day = this_day.nextUntil(".ok");
    if (next_day.length>1){
        for (var i=next_day.length-2; i>0; i--){
            next_day.eq(i).find("input[name$='-day']").val(next_day.eq(i-1).find("input[name$='-day']").val());
            next_day.eq(i).find("span[id$='-day-value']").text(next_day.eq(i-1).find("span[id$='-day-value']").text());
        }
        next_day.eq(0).find("input[name$='-day']").val(this_day.find("input[name$='-day']").val());
        next_day.eq(0).find("span[id$='-day-value']").text(this_day.find("span[id$='-day-value']").text());
    }
    $(this).siblings("input[name$='-DELETE']").attr("checked", true);
    this_day.hide();
}

function deleteNewDay(){
	var vtf = parseInt($("#id_day-TOTAL_FORMS").val());
	$("#id_day-TOTAL_FORMS").val(vtf-1);
	var this_day = $(this).parent().parent();
    var next_day = this_day.nextUntil(".ok");
    var index = parseInt($(this).siblings("input[name$='-day']").attr("name").split("-")[1]);
    var number = $(this).siblings("input[name$='-day']").val();
	if (next_day.length>1){
		for (var i=0; i<next_day.length; i++ ){
            changeDay(index, number, next_day.eq(i));
            index++;number++;
		}
	}
    this_day.remove();
}

function changeDay(index, number, training_day){
    input = training_day.find("input");
    day_value = training_day.find('[id$="-day-value"]');
    for (var i=0; i<input.length;i++){
        input.eq(i).attr("name", function(i, origValue){
            return origValue.replace(/^day-[0-9]+/i,"day-"+index)
        });
        input.eq(i).attr("id", function(i, origValue){
            return origValue.replace(/^id_day-[0-9]+/i,"id_day-"+index)
        });
    }
    input.filter('[id$="-day"]').val(number);
    day_value.text(number);
    day_value.attr("id", function(i, origValue){
        return origValue.replace(/^id_day-[0-9]+/i,"id_day-"+index)
    });
}

function addSets(){
    var total_forms = $(this).siblings('[name$="-sets-TOTAL_FORMS"]');
	var id_total_forms = total_forms.attr("id");
	var day_id = parseInt($("#"+id_total_forms.replace("sets-TOTAL_FORMS","id")).val());
    if (!day_id){ day_id=-1; }
	var vtf = parseInt(total_forms.val());
	var id_prefix = id_total_forms.replace("TOTAL_FORMS", vtf);
    var name_prefix = id_prefix.replace("id_","");
    var number = parseInt($(this).prev().find("input[name$='-number']").val())+1;
    if (!number){ number = 1; }
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
		'<input type="hidden" name="'+name_prefix+'-number" value='+number+' id="'+id_prefix+'-number" ></td></tr>';
	$("#"+id_total_forms).val(vtf+1);
	$(this).before(newSets);
	$("#"+id_prefix+"-number").parent().children(".delete-sets").click(deleteNewSets);
}

function deleteOldSets(){
	var this_sets = $(this).parent().parent();
	var next_sets = this_sets.nextUntil(".addsets");
	if (next_sets.length>0){
		for (var i=next_sets.length-1; i>0; i-- ){
            next_sets.eq(i).find("input[name$='-number']").val(next_sets.eq(i-1).find("input[name$='-number']").val());
        }
		next_sets.eq(0).find("input[name$='-number']").val($(this).siblings("input[name$='-number']").val());
    }
	$(this).siblings("input[name$='-DELETE']").attr("checked", true);
	this_sets.hide();
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
	var inputs1 = sets1.find("input").not("input[name$='-number']");
	var inputs2 = sets2.find("input").not("input[name$='-number']");
	for (var i=0; i<inputs1.length; i++){
		inputs1.eq(i).val(inputs2.eq(i).val());
	}
}