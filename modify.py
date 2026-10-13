from pathlib import Path
p=Path('/tmp/ttsimple/app.js')
s=p.read_text()
s=s.replace('Drag a player onto another player to swap positions, or onto an empty position to move them. Drag a substitute onto a player to replace them. On phones, tap a player and then tap the target position; tap a substitute then the player to replace.', 'Drag players to swap position or sub.')
start=s.index("document.querySelectorAll('[data-pitch-player]').forEach(el=>", s.index('function renderVisualPitch'))
end=s.index("$('visualPitchSubs').addEventListener('dragover'", start)
new="""const dragSources=new Map();let touchDrag=null;function sourceFor(el){if(el.dataset.pitchSub)return {id:el.dataset.pitchSub,sub:true};if(el.dataset.pitchPlayer)return {id:el.dataset.pitchPlayer,index:Number(el.dataset.pitchIndex),sub:false};return null}function applyDrop(src,target){if(!src||!target||!target.dataset.pitchPlayer)return;const targetId=target.dataset.pitchPlayer;if(!targetId)return;const to=Number(target.dataset.pitchIndex);if(src.sub){movePlayer(src.id,to,true)}else{const from=Number(src.index);if(from!==to)movePlayer(from,to,false)}}document.querySelectorAll('[data-pitch-player],[data-pitch-sub]').forEach(el=>{el.addEventListener('dragstart',e=>{const src=sourceFor(el);if(!src)return;selected=src;mark(el);if(e.dataTransfer){e.dataTransfer.effectAllowed='move';e.dataTransfer.setData('text/plain',JSON.stringify(src))}});el.addEventListener('dragover',e=>{if(el.dataset.pitchPlayer&&el.dataset.pitchPlayer){e.preventDefault();if(e.dataTransfer)e.dataTransfer.dropEffect='move'}});el.addEventListener('drop',e=>{if(!el.dataset.pitchPlayer)return;e.preventDefault();let src=null;try{src=JSON.parse(e.dataTransfer?.getData('text/plain')||'null')}catch{}applyDrop(src||selected,el);selected=null});el.addEventListener('pointerdown',e=>{if(e.pointerType!=='touch'&&e.pointerType!=='pen')return;const src=sourceFor(el);if(!src)return;touchDrag={src,el,x:e.clientX,y:e.clientY,moved:false};selected=src;mark(el)});el.addEventListener('pointermove',e=>{if(!touchDrag||touchDrag.el!==el)return;if(Math.hypot(e.clientX-touchDrag.x,e.clientY-touchDrag.y)>8){touchDrag.moved=true;el.style.opacity='.65'}});el.addEventListener('pointerup',e=>{if(!touchDrag||touchDrag.el!==el)return;const d=touchDrag;touchDrag=null;el.style.opacity='';if(!d.moved){selected=null;mark(null);return}e.preventDefault();const target=document.elementFromPoint(e.clientX,e.clientY)?.closest('[data-pitch-player]');if(target)applyDrop(d.src,target);selected=null;mark(null)});el.addEventListener('pointercancel',()=>{if(touchDrag?.el===el){touchDrag=null;el.style.opacity='';selected=null;mark(null)}})});"""
s=s[:start]+new+s[end:]
# Remove empty-position drop to substitutes; no longer support moving to empty slots. Existing drop handler only handles dropping player onto subs, delete it.
old="$('visualPitchSubs').addEventListener('dragover',e=>e.preventDefault());$('visualPitchSubs').addEventListener('drop',e=>{e.preventDefault();let src=null;try{src=JSON.parse(e.dataTransfer?.getData('text/plain')||'null')}catch{}if(src&&!src.sub){const current=pitchPlayerIds(),off=current[src.index];if(off){current[src.index]=null;m().formationSlots=current.slice();m().startingPlayers=current.filter(Boolean);m().activePlayers=(m().activePlayers||[]).filter(id=>id!==off);m().substitutes=[...new Set([...(m().substitutes||[]),off])];snapshot();save();renderVisualPitch()}}});"
s=s.replace(old, "")
p.write_text(s)
# synchronize inline script
idx=Path('/tmp/ttsimple/index.html'); html=idx.read_text(); js=s
script_start=html.index('<script>')+len('<script>'); script_end=html.index('</script>',script_start)
html=html[:script_start]+js+html[script_end:]
# shorten all visual pitch shirts and make touch drag responsive
html=html.replace('.pitchshirt{width:39px;height:43px;', '.pitchshirt{width:30px;height:33px;')
html=html.replace('.pitchslot{border:0;background:transparent;color:#fff;padding:2px;min-width:0;flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;touch-action:pan-y}', '.pitchslot{border:0;background:transparent;color:#fff;padding:2px;min-width:0;flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;touch-action:none;user-select:none;-webkit-user-select:none}')
html=html.replace('.pitchsub{background:#eaf0f6;', '.pitchsub{touch-action:none;user-select:none;-webkit-user-select:none;background:#eaf0f6;')
idx.write_text(html)
# bump cache version
sw=Path('/tmp/ttsimple/sw.js'); st=sw.read_text(); import re
st=re.sub(r'touchline-[A-Za-z0-9_-]+', 'touchline-formation-drag-mobile-v3', st, count=1); sw.write_text(st)
