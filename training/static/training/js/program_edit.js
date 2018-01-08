
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
    var number = parseInt($(this).siblings("input[name$='-day']").val());
	if (next_day.length>1){
		for (var i=0; i<next_day.length; i++ ){
            changeDay(index, number, next_day.eq(i));
            index++;number++;
		}
	}
    this_day.remove();
}

function changeDay(index, number, training_day){
    inputs = training_day.find("input");
    day_value = training_day.find('[id$="-day-value"]');
    for (var i=0; i<inputs.length;i++){
        inputs.eq(i).attr("name", function(i, origValue){
            return origValue.replace(/^day-[0-9]+/i,"day-"+index)
        });
        inputs.eq(i).attr("id", function(i, origValue){
            return origValue.replace(/^id_day-[0-9]+/i,"id_day-"+index)
        });
    }
    inputs.filter('[id$="-day"]').val(number);
    day_value.text(number);
    day_value.attr("id", function(i, origValue){
        return origValue.replace(/^id_day-[0-9]+/i,"id_day-"+index)
    });
}

function addTrainingSets(){
    var total_forms = $(this).siblings('[name$="-sets-TOTAL_FORMS"]');
	var id_total_forms = total_forms.attr("id");
	var day_id = parseInt($("#"+id_total_forms.replace("sets-TOTAL_FORMS","id")).val());
    if (!day_id){ day_id=-1; }
	var vtf = parseInt(total_forms.val());
	var id_prefix = id_total_forms.replace("TOTAL_FORMS", vtf);
    var name_prefix = id_prefix.replace("id_","");
    var number = parseInt($(this).prev().find("input[name$='-number']").val())+1;
    if (!number){ number = 1; }
    var newSets = '<div class="training-sets">'+
    '<div class="exercise-pic">'+
        '<img src="">'+
    '</div>'+
    '<div class="exercise">'+
        '<div class="exercise-name">'+
            '<input type="hidden" name="'+name_prefix+'-exercises" value="" id="'+id_prefix+'-exercises">'+
            '<a></a>'+
            '<ul><h6>备选动作</h6>'+
                '<li data-url="">'+
                    '<a></a>'+
                '</li>'+
            '</ul>'+
        '</div>'+
        '<div class="sets-detail">'+
            '<input type="number" name="'+name_prefix+'-minreps" value="8" min="0" id="'+id_prefix+'-minreps">~<input type="number" name="'+name_prefix+'-maxreps" value="12" min="0" id="'+id_prefix+'-maxreps">RM × <input type="number" name="'+name_prefix+'-sets" value="5" min="0" id="'+id_prefix+'-sets">组&nbsp;&nbsp;休息:<input type="number" name="'+name_prefix+'-rest" value="120" min="0" id="'+id_prefix+'-rest">s</span>'+
        '</div>'+
    '</div>'+
    '<button type="button" class="delete-sets">×</button>'+
    '<input type="hidden" name="'+name_prefix+'-trainingday" value='+day_id+' id="'+id_prefix+'-trainingday">'+
    '<input type="hidden" name="'+name_prefix+'-number" value='+number+' id="'+id_prefix+'-number">'+
    '</div>';
	$("#"+id_total_forms).val(vtf+1);
	$(this).before(newSets);
    $("#"+id_prefix+"-number").siblings(".delete-sets").click(deleteNewSets);
    $("#"+id_prefix+"-exercises").siblings("a").click(openExercisesDialog);
    $("#"+id_prefix+"-exercises").siblings("a").click();
}

function deleteOldSets(){
	var this_sets = $(this).parent();
	var next_sets = this_sets.nextUntil(".add-training-sets");
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
	var this_sets = $(this).parent();
    var next_sets = this_sets.nextUntil(".add-training-sets");
    var index = parseInt($(this).siblings("input[name$='-number']").attr("name").split("-")[3]);
    var number = parseInt($(this).siblings("input[name$='-number']").val());
	for (var i=0; i<next_sets.length; i++ ){
        changeSets(index, number, next_sets.eq(i));
        index++;number++;
	}
    this_sets.remove();
}

function changeSets(index, number, sets){
    inputs = sets.find("input");
    for (var i=0; i<inputs.length;i++){
        inputs.eq(i).attr("name", function(i, origValue){
            return origValue.replace(/-sets-[0-9]+/i,"-sets-"+index)
        });
        inputs.eq(i).attr("id", function(i, origValue){
            return origValue.replace(/-sets-[0-9]+/i,"-sets-"+index)
        });
    }
    inputs.filter('[id$="-number"]').val(number);
}

function openExercisesDialog(){
    var input = $(this).siblings("input");
    $("#sets-exercises-id").text(input.attr("id"));
    $("#chosen-exercises-id").text(input.val());
    var names = [];
    var pic_url = [];
    $(this).siblings("ul").find("li").each(function(){
        names.push($(this).text());
        pic_url.push($(this).attr("data-url"));
    });
    $(".ui-dialog-buttonset").children().first().text("已选动作: "+names.join());
    $("#chosen-exercises-pic").text(pic_url.join());
    $(".selected").removeClass("selected");
    $(".exercise-list").accordion( "option", "active", false );
    input.val().split(",").forEach(function(item){ 
        var item_div = $(".select-exercise[data-id='"+item+"']");
        item_div.addClass("selected");
        item_div.parent().parent().accordion( "option", "active", 0 );
    });
    $("#exercises-dialog").dialog("open");
}

function dialogConfirm(){
    var ids = $("#chosen-exercises-id").text();
    if ( !ids ){
        alert("请选择至少一个动作！")
    }else{
        var names = $(".ui-dialog-buttonset").children().first().text().replace("已选动作: ", "");
        var target = $("#"+$("#sets-exercises-id").text());
        var pic_url = $("#chosen-exercises-pic").text().split(",");
        target.val(ids);
        target.siblings("a").text(names.split(",")[0]);
        target.siblings("ul").children("li").remove();
        names.split(",").forEach(function(item, index){
            target.siblings("ul").append('<li data-url="'+pic_url[index]+'"><a>'+item+'</a></li>');
        });
		target.siblings("ul").children("li").each(function(){
			$(this).click(function(){
				$(this).parent().siblings("a").text($(this).text());
				$(this).parent().parent().parent().siblings(".exercise-pic").children("img").attr("src", $(this).attr("data-url"));
			});
        });
        target.siblings("ul").children("li").first().click();
        $("#exercises-dialog").dialog("close");
    }
}

function dialogClose(){
    var target = $("#"+$("#sets-exercises-id").text());
    if (!target.val()){
        alert("请选择至少一个动作！")
    }else{
        $("#exercises-dialog").dialog( "close" );
    }
}

function checkItem(){
    var ids = $("#chosen-exercises-id").text();
    if(ids==""){ ids=[]; }else{ ids=ids.split(","); }
    var pic_url = $("#chosen-exercises-pic").text();
    if(pic_url==""){ pic_url=[]; }else{ pic_url=pic_url.split(","); }
    var names = $(".ui-dialog-buttonset").children().first().text().replace("已选动作: ", "");
    if(names==""){ names=[]; }else{ names=names.split(","); }
    var this_id = $(this).attr("data-id");
    var this_pic = $(this).attr("data-url");
    var this_name = $(this).text();
    index = ids.indexOf(this_id);
    if (index==-1){
        ids.push(this_id);
        names.push(this_name);
        pic_url.push(this_pic);
    }else{
        ids.splice(index,1)
        names.splice(index,1)
        pic_url.splice(index,1)
    }
    $(this).toggleClass("selected");
    $("#chosen-exercises-id").text(ids.join());
    $("#chosen-exercises-pic").text(pic_url.join());
    $(".ui-dialog-buttonset").children().first().text("已选动作: "+names.join());
}
