var ws;
var isSetup = false;
         
function init() {

  // Connect to Web Socket
  ws = new WebSocket("ws://192.168.91.127:9001/");

  // Set event handlers.
  ws.onopen = function() {
    output("onopen");
  };
  
  ws.onmessage = function(e) {
    // e.data contains received string.
    output("onmessage: " + e.data);
  };
  
  ws.onclose = function() {
    output("onclose");
  };

  ws.onerror = function(e) {
    output("onerror");
    console.log(e)
  };

}

function setBellOne(){
  isSetup = true;
  var bellOneCode = document.getElementById("bellOneCode");
  // You can send message to the Web Socket using ws.send.
  bellOneCode.value = "Hangra vár";
}

function playKeyboard() {
  let isMobile = !!navigator.userAgent.match(
  /Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile/i);

  let events;



  function useBell(playedNote) {
    ws.send(playedNote);
  }

  isMobile ?
  events = ["touchstart", "touchend"] :
  events = ["mousedown", "mouseup"];

  let audioSynth = new AudioSynth();
  audioSynth.setVolume(0.5);

  let octave = 4;

  let keyboard = {
    192: "C,-2", // ~
    49: "C#,-2", // 1
    50: "D,-2", // 2
    51: "D#,-2", // 3
    52: "E,-2", // 4
    53: "F,-2", // 5
    54: "F#,-2", // 6
    55: "G,-2", // 7
    56: "G#,-2", // 8
    57: "A,-2", // 9
    48: "A#,-2", // 0
    189: "B,-2", // -
    187: "C,-1", // =
    81: "C#,-1", // q
    87: "D,-1", // w
    69: "D#,-1", // e
    82: "E,-1", // r
    84: "F,-1", // t
    89: "F#,-1", // y
    85: "G,-1", // u
    73: "G#,-1", // i
    79: "A,-1", // o
    80: "A#,-1", // p
    219: "B,-1", // [
    221: "C,0", // ]
    65: "C#,0", // a
    83: "D,0", // s
    68: "D#,0", // d
    70: "E,0", // f
    71: "F,0", // g
    72: "F#,0", // h
    74: "G,0", // j
    75: "G#,0", // k
    76: "A,0", // l
    186: "A#,0", // ;
    222: "B,0", // "
    90: "C,1", // z
    88: "C#,1", // x
    67: "D,1", // c
    86: "D#,1", // v
    66: "E,1", // b
    78: "F,1", // n
    77: "F#,1", // m
    188: "G,1", // ,
    190: "G#,1", // .
    191: "A,1", // /
    37: "A#,1", // <
    39: "B,1" // >
  };

  let reverseLookupText = {},
  reverseLookup = {};

  for (let i in keyboard) {
    let val;

    switch (i | 0) {
      case 187:
        val = 61;
        break;
      case 219:
        val = 91;
        break;
      case 221:
        val = 93;
        break;
      case 188:
        val = 44;
        break;
      case 190:
        val = 46;
        break;
      default:
        val = i;
        break;}


    reverseLookup[keyboard[i]] = i;
    reverseLookupText[keyboard[i]] = val;
  }

  let keysPressed = [];

  let visualKeyboard = document.getElementById("keyboard");

  let selectSound = {
    value: "0" };


  let iKeys = 0;
  let iWhite = 0;
  let notes = audioSynth._notes;

  for (let i = -2; i <= 1; i++) {
    for (let n in notes) {
      if (n[2] != "b") {
        let thisKey = document.createElement("div");

        if (n.length > 1) {
          thisKey.className = "key black";
          thisKey.style.left = 40 * (iWhite - 1) + 25 + "px";
        } else {
          thisKey.className = "key white";
          thisKey.style.left = 40 * iWhite + "px";
          iWhite++;
        }

        let label = document.createElement("div");
        label.className = "label";

        let s = getDispStr(n, i, reverseLookupText);

        label.innerHTML =
        "<span>" +
        s +
        "</span>" +
        "<span name='octavel-label' value='" +
        i +
        "'>" +
        n.substr(0, 1) +
        "" + (
        octave + parseInt(i)) +
        "" + (
        n.substr(1, 1) ? n.substr(1, 1) : "");
        "</span>";

        thisKey.appendChild(label);
        thisKey.setAttribute("id", "key" + n + "," + i);
        thisKey.addEventListener(
        events[0],
        (temp => {
          return function () {
            fnPlayKeyboard({ keyCode: temp });
          };
        })(reverseLookup[n + "," + i]));

        visualKeyboard[n + "," + i] = thisKey;
        visualKeyboard.appendChild(thisKey);

        iKeys++;
      }
    }
  }

  window.addEventListener(events[1], () => {
    n = keysPressed.length;

    while (n--) {
      fnRemoveKeyBinding({ keyCode: keysPressed[n] });
    }
  });

  function fnPlayKeyboard(e) {
    let i = keysPressed.length;

    while (i--) {
      if (keysPressed[i] == e.keyCode) {
        return false;
      }
    }

    keysPressed.push(e.keyCode);

    if (keyboard[e.keyCode]) {
      if (visualKeyboard[keyboard[e.keyCode]]) {
        visualKeyboard[keyboard[e.keyCode]].classList.add("is-playing");
      }

      let arrPlayNote = keyboard[e.keyCode].split(",");
      let note = arrPlayNote[0];
      let octaveModifier = arrPlayNote[1] | 0;

      if(isSetup){
        var setupString = "Setup"
      useBell(setupString.concat(keyboard[e.keyCode]));
      isSetup = false;
      var bellOneCode = document.getElementById("bellOneCode");
      var templateText = "Az 1-es harang hangja: "
      bellOneCode.value = templateText.concat();
    }
    else{
      var playString = "Play"
      useBell(playString.concat(keyboard[e.keyCode]));
    }
      //fnPlayNote(note, octave + octaveModifier);
    } else {
      return false;
    }
  }

  function fnRemoveKeyBinding(e) {
    let i = keysPressed.length;

    while (i--) {
      if (keysPressed[i] == e.keyCode) {
        if (visualKeyboard[keyboard[e.keyCode]]) {
          visualKeyboard[keyboard[e.keyCode]].classList.remove("is-playing");
        }

        keysPressed.splice(i, 1);
      }
    }
  }

  function fnPlayNote(note, octave) {
    src = audioSynth.generate(selectSound.value, note, octave, 2);
    container = new Audio(src);

    container.addEventListener("ended", () => {
      container = null;
    });

    container.addEventListener("loadeddata", e => {
      e.target.play();
    });

    container.autoplay = false;
    container.setAttribute("type", "audio/wav");
    container.load();

    return container;
  }

  function getDispStr(n, i, lookup) {
    if (n == "C" && i == -2) {
      return "~";
    } else if (n == "B" && i == -2) {
      return "-";
    } else if (n == "A#" && i == 0) {
      return ";";
    } else if (n == "B" && i == 0) {
      return '"';
    } else if (n == "A" && i == 1) {
      return "/";
    } else if (n == "A#" && i == 1) {
      return "<-";
    } else if (n == "B" && i == 1) {
      return "->";
    } else {
      return String.fromCharCode(lookup[n + "," + i]);
    }
  }

  window.addEventListener("keydown", fnPlayKeyboard);
  window.addEventListener("keyup", fnRemoveKeyBinding);
}

document.addEventListener("DOMContentLoaded", () => {
  playKeyboard();
});