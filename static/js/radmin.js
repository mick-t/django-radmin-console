/* Puts the included jQuery into our own namespace using noConflict and passing
 *  * it 'true'. This ensures that the included jQuery doesn't pollute the global
 *   * namespace (i.e. this preserves pre-existing values for both window.$ and
 *    * window.jQuery).
 *     */
var radmin = {
	    "jQuery": jQuery.noConflict(true)
};

$r = radmin.jQuery;

radmin.init = function(ctx){
	// gets called even before dom is ready
	radmin.ctx = JSON.parse(ctx);
}

$r(function(){
	// Once the dom is ready, continue
	// do the request to radmin
	$r.get("/radmin/ep/", radmin.ctx, function(data){
		radmin.build_ui(data);
	});
});


radmin.build_ui = function(data){
	// we are gonna hijack the django admin container  a bit
	var container = document.getElementById("container");
	var header = document.getElementById("header");
	var console_wrap = document.createElement('div');
	console_wrap.id = "radmin-console-wrap";
	container.appendChild(console_wrap);
	//reposition radmin based on its header
	console_wrap.style.top =  header.scrollHeight + "px";
	radmin.cw = console_wrap;
	// add controls where appropriate
	for(d in data){
		radmin.add_control(data[d]);
	}
}

radmin.control_meta = {} // stores data by key

radmin.add_control = function(item){
	var btn_wrap = document.createElement('span')
	var btn = document.createElement('button');
	btn_wrap.className="radmin-control-btn-wrap";
	btn.id = item.target;
	btn.innerText = item.label;
	btn.addEventListener('click',radmin.runcommand);
	// also store any data item in the control_meta
	if(item.data != undefined && item.data != null && item.data != ''){
		radmin.control_meta[item.target] = item.data;
	}
	btn_wrap.appendChild(btn);
	radmin.cw.appendChild(btn_wrap);
}

radmin.runcommand = function(e){
	var caller = e.target;
	var loadicon = document.createElement('span');
	loadicon.className='radmin-loading';
	caller.parentNode.appendChild(loadicon);
	meta = radmin.control_meta[caller.id];
	if(meta!=undefined){
		data = {'target':caller.id, 'data':meta}
	}else{
		data = {'target':caller.id}
	}
	$r.get("/radmin/rnr/", data, function(data){
		$r(loadicon).remove();
		// display message if appropriate
		if(data.display_result){
			radmin.make_mssg(data.output);
		}
	});
	
}

radmin.make_mssg = function(output){
	console.log(output);
}




