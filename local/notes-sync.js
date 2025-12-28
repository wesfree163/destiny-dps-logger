async function loadAllNotes() {
  try {
    const r = await fetch("notes.json");
    const data = await r.json();

    for (const key in data) {
      localStorage.setItem(key, data[key]);
    }
  } catch (e) {
    console.log("No notes.json yet");
  }
}

async function saveAllNotes() {
  const notes = {};
  for (let k in localStorage) {
    if (k.startsWith("note-")) notes[k] = localStorage[k];
  }

  const blob = new Blob([JSON.stringify(notes, null, 2)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "notes.json";
  a.click();
}
