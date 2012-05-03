# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import Organization
import Repository
import NamedUser

class Event( object ):
    def __init__( self, github, attributes, lazy ):
        self.__github = github
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def actor( self ):
        self.__completeIfNeeded( self.__actor )
        return self.__actor

    @property
    def commit_id( self ):
        self.__completeIfNeeded( self.__commit_id )
        return self.__commit_id

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def event( self ):
        self.__completeIfNeeded( self.__event )
        return self.__event

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def issue( self ):
        self.__completeIfNeeded( self.__issue )
        return self.__issue

    @property
    def org( self ):
        self.__completeIfNeeded( self.__org )
        return self.__org

    @property
    def payload( self ):
        self.__completeIfNeeded( self.__payload )
        return self.__payload

    @property
    def public( self ):
        self.__completeIfNeeded( self.__public )
        return self.__public

    @property
    def repo( self ):
        self.__completeIfNeeded( self.__repo )
        return self.__repo

    @property
    def type( self ):
        self.__completeIfNeeded( self.__type )
        return self.__type

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__actor = None
        self.__commit_id = None
        self.__created_at = None
        self.__event = None
        self.__id = None
        self.__issue = None
        self.__org = None
        self.__payload = None
        self.__public = None
        self.__repo = None
        self.__type = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        result = self.__github._dataRequest(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( result )
        self.__completed = True

    def __useAttributes( self, attributes ):
        if "actor" in attributes:
            self.__actor = attributes[ "actor" ]
        if "commit_id" in attributes:
            self.__commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes:
            self.__created_at = attributes[ "created_at" ]
        if "event" in attributes:
            self.__event = attributes[ "event" ]
        if "id" in attributes:
            self.__id = attributes[ "id" ]
        if "issue" in attributes:
            self.__issue = attributes[ "issue" ]
        if "org" in attributes:
            self.__org = attributes[ "org" ]
        if "payload" in attributes:
            self.__payload = attributes[ "payload" ]
        if "public" in attributes:
            self.__public = attributes[ "public" ]
        if "repo" in attributes:
            self.__repo = attributes[ "repo" ]
        if "type" in attributes:
            self.__type = attributes[ "type" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
