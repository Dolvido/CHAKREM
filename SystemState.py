
import sqlite3
import json

class SystemState:
    def __init__(self):
        self.user_info = {
            "input": None,
            "input_history": [],
            "session_data": {
                "start_time": None,
                "duration": None,
            }
        }
        self.agent_info = {
            # Will be filled dynamically as agents are added to the system
        }
        self.system_metrics = {
            "response_times": [],
            "error_logs": [],
        }
        self.environmental_data = {
            "date_time": None,
            "external_apis": {},
        }
        self.session_flags = {
            "urgent_request": False,
            "emotional_state": None,
        }
        self.miscellaneous = {}

        # Database connection
        self.conn = sqlite3.connect('system_states.db')
        
        # Create the database table
        self._create_db_table()

    def update_user_input(self, input_text):
        """Update the current user input and append it to the input history."""
        self.user_info['input'] = input_text
        self.user_info['input_history'].append(input_text)


    def _create_db_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS system_states (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_info TEXT,
                agent_info TEXT,
                system_metrics TEXT,
                environmental_data TEXT,
                session_flags TEXT,
                miscellaneous TEXT
            )
        ''')

    def insert_system_state(self):
        # Serialize aspects of the system state to JSON strings
        user_info_json = json.dumps(self.user_info)
        agent_info_json = json.dumps(self.agent_info)
        system_metrics_json = json.dumps(self.system_metrics)
        environmental_data_json = json.dumps(self.environmental_data)
        session_flags_json = json.dumps(self.session_flags)
        miscellaneous_json = json.dumps(self.miscellaneous)

        # Insert a new row in the database with the serialized data
        self.conn.execute('''
            INSERT INTO system_states (
                user_info, agent_info, system_metrics, environmental_data, session_flags, miscellaneous
            ) VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_info_json, agent_info_json, system_metrics_json, environmental_data_json, session_flags_json, miscellaneous_json))
        self.conn.commit()

    def get_system_states(self):
        # Retrieve all rows from the system states table in the database
        cursor = self.conn.execute('SELECT * FROM system_states')

        # Create a list to hold the SystemState objects
        system_states = []

        # For each row, create a new SystemState object and populate it with the data from the row
        for row in cursor:
            new_state = SystemState()
            new_state.user_info = json.loads(row[1])
            new_state.agent_info = json.loads(row[2])
            new_state.system_metrics = json.loads(row[3])
            new_state.environmental_data = json.loads(row[4])
            new_state.session_flags = json.loads(row[5])
            new_state.miscellaneous = json.loads(row[6])
            system_states.append(new_state)

        return system_states

    def close_db(self):
        self.conn.close()
