from omero_ark.rath import OmeroArkRath
from datetime import datetime
from pydantic import Field, BaseModel
from typing_extensions import Literal
from typing import List, Tuple, Optional
from omero_ark.funcs import aexecute, execute
from enum import Enum
from rath.scalars import ID


class OmerUserInput(BaseModel):
    username: str
    password: str

    class Config:
        frozen = True
        extra = "forbid"
        use_enum_values = True


class EnsureOmeroUserMutationEnsureomerouserUser(BaseModel):
    typename: Optional[Literal["User"]] = Field(alias="__typename", exclude=True)
    id: ID
    sub: str

    class Config:
        frozen = True


class EnsureOmeroUserMutationEnsureomerouser(BaseModel):
    typename: Optional[Literal["OmeroUser"]] = Field(alias="__typename", exclude=True)
    id: ID
    omero_username: str = Field(alias="omeroUsername")
    omero_password: str = Field(alias="omeroPassword")
    user: EnsureOmeroUserMutationEnsureomerouserUser

    class Config:
        frozen = True


class EnsureOmeroUserMutation(BaseModel):
    ensure_omero_user: EnsureOmeroUserMutationEnsureomerouser = Field(
        alias="ensureOmeroUser"
    )

    class Arguments(BaseModel):
        username: str
        password: str

    class Meta:
        document = "mutation EnsureOmeroUser($username: String!, $password: String!) {\n  ensureOmeroUser(input: {username: $username, password: $password}) {\n    id\n    omeroUsername\n    omeroPassword\n    user {\n      id\n      sub\n    }\n  }\n}"


class ListProjectsQueryProjectsDatasetsImages(BaseModel):
    typename: Optional[Literal["Image"]] = Field(alias="__typename", exclude=True)
    name: str
    acquisition_date: Optional[datetime] = Field(alias="acquisitionDate")

    class Config:
        frozen = True


class ListProjectsQueryProjectsDatasets(BaseModel):
    typename: Optional[Literal["Dataset"]] = Field(alias="__typename", exclude=True)
    name: str
    description: str
    images: Tuple[ListProjectsQueryProjectsDatasetsImages, ...]

    class Config:
        frozen = True


class ListProjectsQueryProjects(BaseModel):
    typename: Optional[Literal["Project"]] = Field(alias="__typename", exclude=True)
    name: str
    description: str
    datasets: Tuple[ListProjectsQueryProjectsDatasets, ...]

    class Config:
        frozen = True


class ListProjectsQuery(BaseModel):
    projects: Tuple[ListProjectsQueryProjects, ...]

    class Arguments(BaseModel):
        pass

    class Meta:
        document = "query ListProjects {\n  projects {\n    name\n    description\n    datasets {\n      name\n      description\n      images {\n        name\n        acquisitionDate\n      }\n    }\n  }\n}"


async def aensure_omero_user(
    username: str, password: str, rath: OmeroArkRath = None
) -> EnsureOmeroUserMutationEnsureomerouser:
    """EnsureOmeroUser



    Arguments:
        username (str): username
        password (str): password
        rath (omero_ark.rath.OmeroArkRath, optional): The omero_ark rath client

    Returns:
        EnsureOmeroUserMutationEnsureomerouser"""
    return (
        await aexecute(
            EnsureOmeroUserMutation,
            {"username": username, "password": password},
            rath=rath,
        )
    ).ensure_omero_user


def ensure_omero_user(
    username: str, password: str, rath: OmeroArkRath = None
) -> EnsureOmeroUserMutationEnsureomerouser:
    """EnsureOmeroUser



    Arguments:
        username (str): username
        password (str): password
        rath (omero_ark.rath.OmeroArkRath, optional): The omero_ark rath client

    Returns:
        EnsureOmeroUserMutationEnsureomerouser"""
    return execute(
        EnsureOmeroUserMutation, {"username": username, "password": password}, rath=rath
    ).ensure_omero_user


async def alist_projects(rath: OmeroArkRath = None) -> List[ListProjectsQueryProjects]:
    """ListProjects



    Arguments:
        rath (omero_ark.rath.OmeroArkRath, optional): The omero_ark rath client

    Returns:
        List[ListProjectsQueryProjects]"""
    return (await aexecute(ListProjectsQuery, {}, rath=rath)).projects


def list_projects(rath: OmeroArkRath = None) -> List[ListProjectsQueryProjects]:
    """ListProjects



    Arguments:
        rath (omero_ark.rath.OmeroArkRath, optional): The omero_ark rath client

    Returns:
        List[ListProjectsQueryProjects]"""
    return execute(ListProjectsQuery, {}, rath=rath).projects
