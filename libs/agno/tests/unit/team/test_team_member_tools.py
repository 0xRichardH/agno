from agno.models.response import ToolExecution
from agno.run.response import RunEvent, RunResponse
from agno.run.team import TeamRunResponse


def test_team_run_response_includes_member_tools():
    tool = ToolExecution(tool_name="echo", result="hi")
    member_resp = RunResponse(event=RunEvent.run_response, tools=[tool], agent_id="a1")
    team_resp = TeamRunResponse()
    team_resp.add_member_run(member_resp)

    result = team_resp.to_dict()
    assert "member_responses" in result
    assert result["member_responses"][0]["tools"][0]["tool_name"] == "echo"
