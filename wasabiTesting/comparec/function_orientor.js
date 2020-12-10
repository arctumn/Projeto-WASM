    var listOfElements = [];
    Wasabi.analysisResult = listOfElements;

    function fctName(fctId) {
        const fct = Wasabi.module.info.functions[fctId];
        if (fct.export[0] !== undefined) return "wasm_outer_export_"+ fct.export[0];
        if (fct.import !== null) return "wasm_outer_import_"+ fct.import;
        return "wasm_inner_id_" + fctId;
    }

    function parseType(serializedType){
        if (serializedType === "") return "Received void, Returned void"

        parsedString = "Received args: "

        //Parsing if the input is empty and if is not empty
        if (serializedType.charAt(0) === '|') parsedString += "void"

        serializedType.split('').forEach(function(letter)  {
                switch (letter) {
                    case 'i':
                        parsedString = parsedString + "i32 "
                        break;
                    case 'I':
                        parsedString = parsedString + "i64 "
                        break;
                    case 'f':
                        parsedString = parsedString + "f32 "
                        break;
                    case 'F':
                        parsedString = parsedString + "f64 "
                        break;
                    case '|':
                        parsedString = parsedString + "; Returning args: "
                        break;
                    default:
                        break;
                }
            })

        if (serializedType.charAt(serializedType.length - 1) === '|') parsedString += "void"
        
        return parsedString
        }

        function argType(fctId){
            const fct = Wasabi.module.info.functions[fctId];
            return parseType(fct.type)
        }
    Wasabi.analysis = {
        call_pre(location, targetFunc, args, indirectTableIdx) {
            const caller = fctName(location.func);
            const callee = fctName(targetFunc);
            const argcallee = argType(targetFunc);
                listOfElements.push("The function "+ caller + " is using the function " + callee + "("+argcallee+")");
          
        },
    };

    (function (console) {
        console.save = function (data, filename) {
            if (!data) {
                console.error('Console.save: No data')
                return;
            }
    
            if (!filename) filename = 'console.json'
    
            if (typeof data === "object") {
                data = JSON.stringify(data, undefined, 4)
            }
    
            var blob = new Blob([data], { type: 'text/json' }),
                e = document.createEvent('MouseEvents'),
                a = document.createElement('a')
    
            a.download = filename
            a.href = window.URL.createObjectURL(blob)
            a.dataset.downloadurl = ['text/json', a.download, a.href].join(':')
            e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
            a.dispatchEvent(e)
        }
    })(console);
    

function write(list){
    let infofile = "-----------Function_calls.txt-----------\n";
    list.forEach(element => {
        //console.log("Still Going");
        infofile += "function call:\n "+element+ '\n';
    });
    console.save(infofile,"Function_calls.txt")
}
   

