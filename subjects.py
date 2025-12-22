from pyscript import document

# nested dictionaries :3
subject_data = {
	'linguistics': {
		'name': 'Linguistics',
		'icon': 'LNA.png',
		'description': 'Do not wander into restricted areas during class.',
		'professor': 'Nightmare Archivist',
		'topics': [
			'...'
		],
		'classroom': 'Library, Main Hall'
	},
	'science': {
		'name': 'Science',
		'icon': 'HPRA.png',
		'description': 'Deal with all sorts of dangerous chemicals. That is all.',
		'professor': 'Regretful Alchemist',
		'topics': [
			'...'
		],
		'classroom': 'Laboratory'
	},
	'history': {
		'name': 'History',
		'icon': 'LNA.png',
		'description': 'Powers lay on the other side of the Dimensional Portal. Students learn to protect the Academy.',
		'professor': 'Nightmare Archivist',
		'topics': [
			'...'
		],
		'classroom': 'Library, Main Hall'
	},
	'agriculture': {
		'name': 'Agriculture',
		'icon': 'AWL.png',
		'description': 'Located on a stone path routed around a garden of neatly maintained, cubic hedges. Pure Vanilla and White Lily spent a lot of their time here.',
		'professor': 'White Lily Cookie',
		'topics': [
			'...'
		],
		'classroom': 'Front Gardens, Greenhouse'
	},
	'potions': {
		'name': 'Potion Brewing',
		'icon': 'HPRA.png',
		'description': 'Do not be that person brewing a love potion... or do.',
		'professor': 'Regretful Alchemist',
		'topics': [
			'...'
		],
		'classroom': 'Laboratory'
	},
	'pe': {
		'name': 'Physical Education',
		'icon': 'PELT.png',
		'description': 'Shadow Milk Cookie will always outsmart you... or will he? Train here to find out.',
		'professor': 'Labyrinth Tactician',
		'topics': [
			'...'
		],
		'classroom': 'Gymnasium'
	},
	'sorcery': {
		'name': 'Advanced Sorcery',
		'icon': 'Bachalomoth_the_Dreamer.png',
		'description': 'Only for those who wish to venture beyond. Will you open the portal and see the other side?',
		'professor': 'Bachalomoth the Dreamer',
		'topics': [
			'The Moonstone'
			'The Dimensional Portal'
			'The Perfect Cookie'
		],
		'classroom': 'Hall of Enlightenment, Observatory'
	}
}

# even the functions are nested :3 ... the first ones can be found in the HTML, the second ones are aaaalll here
def show_club_linguistics(event):
	show_club_info('linguistics')

def show_club_science(event):
	show_club_info('science')

def show_club_history(event):
	show_club_info('history')

def show_club_agriculture(event):
	show_club_info('agriculture')

def show_club_potions(event):
	show_club_info('potions')

def show_club_pe(event):
	show_club_info('pe')

def show_club_sorcery(event):
	show_club_info('sorcery')

def show_club_info(subject_key):
	if subject_key in subject_data:
		subject = subject_data[subject_key]
		
		activities_html = ''.join([f'<li style="margin-bottom: 0.5rem;">• {topics}</li>' for topics in subject['topics']])
		
		# thank you claude ai for helping me figure that out... I wanted an image </3
		subject_html = f"""
		<div class="icon">
			<img src="{subject['icon']}" alt="{subject['name']}" style="width: 200px; height: 200px; object-fit: contain; margin-bottom: 1.5rem;">
		</div>
		<h3>{subject['name']}</h3>
		<p style="font-size: 1.1rem; margin-bottom: 2rem;">{subject['description']}</p>
		
		<div style="text-align: left; max-width: 600px; margin: 0 auto;">
			<div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem;">
				<p style="margin: 0;"><strong style="color: #e0d5ff;">Overseer:</strong> {subject['professor']}</p>
			</div>
			
			<div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem;">
				<p style="margin-bottom: 1rem;"><strong style="color: #e0d5ff;">Topics:</strong></p>
				<ul style="list-style: none; padding: 0; margin: 0;">
					{activities_html}
				</ul>
			</div>
			
			<div style="background: rgba(255, 255, 255, 0.1); padding: 1.5rem; border-radius: 15px;">
				<p style="margin: 0;"><strong style="color: #e0d5ff;">Classroom:</strong> {subject['classroom']}</p>
			</div>
		</div>
		"""
		
		document.getElementById('subject-display').innerHTML = subject_html