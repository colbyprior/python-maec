#MAEC Object History Classes

#Copyright (c) 2014, The MITRE Corporation
#All rights reserved

#Compatible with MAEC v4.1
#Last updated 08/25/2014

class ObjectHistory(object):
    @classmethod
    def build(cls, bundle):
        """Build the Object History for a Bundle"""
        cls.entries = [] # A list of the Objects in the Object History
        # Get the Objects that are not references
        objects = bundle.get_all_non_reference_objects()
        for object in objects:
            object_history_entry = ObjectHistoryEntry(object)
            # Find and set all Actions that operate on the Object
            if bundle.get_all_actions_on_object(object):
                object_history_entry.actions = bundle.get_all_actions_on_object(object)
            # Add the history entry to the list
            cls.entries.append(object_history_entry)

class ObjectHistoryEntry(object):
    def __init__(self, object = None):
        self.object = object
        self.actions = [] # A list of the Actions that operate on the Object
        self.behaviors = [] # A list of Behaviors that make use of the Object (through Actions?)

    def get_action_names(self):
        """Return a list of the Actions that operated on the Object, via their names"""
        return [x.name.value for x in self.actions if x.name]
