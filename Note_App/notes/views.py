from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def note_list(request):
    notes = Note.objects.all()
    note_count = notes.count()
    return render(request, 'note_list.html', {'notes': notes, 'note_count': note_count})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
        return render(request, 'add_note.html', {'form': form})
    
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('note_list')
