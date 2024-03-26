<div align="center">

[![Visit Inducedai](./header.png)](https://induced.ai)

# Inducedai<a id="inducedai"></a>

Building the next evolution of actionable AI.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`inducedai.autonomous.get_result`](#inducedaiautonomousget_result)
  * [`inducedai.autonomous.terminate_task`](#inducedaiautonomousterminate_task)
  * [`inducedai.extraction.from_url`](#inducedaiextractionfrom_url)
  * [`inducedai.extraction.get_result`](#inducedaiextractionget_result)
  * [`inducedai.feedback.submission`](#inducedaifeedbacksubmission)
  * [`inducedai.task.execute`](#inducedaitaskexecute)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=InducedAI&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from induced_ai_python_sdk import InducedAi, ApiException

inducedai = InducedAi(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Get Autonomous Task Result
    get_result_response = inducedai.autonomous.get_result(
        id="id_example",
    )
    print(get_result_response)
except ApiException as e:
    print("Exception when calling AutonomousApi.get_result: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from induced_ai_python_sdk import InducedAi, ApiException

inducedai = InducedAi(
    api_key_auth="YOUR_API_KEY",
)


async def main():
    try:
        # Get Autonomous Task Result
        get_result_response = await inducedai.autonomous.aget_result(
            id="id_example",
        )
        print(get_result_response)
    except ApiException as e:
        print("Exception when calling AutonomousApi.get_result: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from induced_ai_python_sdk import InducedAi, ApiException

inducedai = InducedAi(
    api_key_auth="YOUR_API_KEY",
)

try:
    # Get Autonomous Task Result
    get_result_response = inducedai.autonomous.raw.get_result(
        id="id_example",
    )
    pprint(get_result_response.body)
    pprint(get_result_response.body["success"])
    pprint(get_result_response.body["data"])
    pprint(get_result_response.body["request_id"])
    pprint(get_result_response.body["time_taken"])
    pprint(get_result_response.headers)
    pprint(get_result_response.status)
    pprint(get_result_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AutonomousApi.get_result: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `inducedai.autonomous.get_result`<a id="inducedaiautonomousget_result"></a>

Get Autonomous Task Result

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_result_response = inducedai.autonomous.get_result(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AutonomousGetResultResponse`](./induced_ai_python_sdk/pydantic/autonomous_get_result_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/autonomous/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `inducedai.autonomous.terminate_task`<a id="inducedaiautonomousterminate_task"></a>

Stop an Autonomous Task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
inducedai.autonomous.terminate_task(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/autonomous/{id}/stop` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `inducedai.extraction.from_url`<a id="inducedaiextractionfrom_url"></a>

Extract data from a URL

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
from_url_response = inducedai.extraction.from_url(
    url="string_example",
    query="string_example",
    columns="string_example",
    limit=1,
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### url: `str`<a id="url-str"></a>

##### query: `str`<a id="query-str"></a>

##### columns: `str`<a id="columns-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### format: `str`<a id="format-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ExtractionFromUrlRequest`](./induced_ai_python_sdk/type/extraction_from_url_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ExtractionFromUrlResponse`](./induced_ai_python_sdk/pydantic/extraction_from_url_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/extract` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `inducedai.extraction.get_result`<a id="inducedaiextractionget_result"></a>

Get extraction result

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_result_response = inducedai.extraction.get_result(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ExtractionGetResultResponse`](./induced_ai_python_sdk/pydantic/extraction_get_result_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/extract/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `inducedai.feedback.submission`<a id="inducedaifeedbacksubmission"></a>

Provide Feedback for an Autonomous Task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
inducedai.feedback.submission(
    id="id_example",
    feedback=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### feedback: `bool`<a id="feedback-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FeedbackSubmissionRequest`](./induced_ai_python_sdk/type/feedback_submission_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/autonomous/{id}/feedback` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `inducedai.task.execute`<a id="inducedaitaskexecute"></a>

Execute an Autonomous Task

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
execute_response = inducedai.task.execute(
    task="Go to google and search for Elon Musk",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### task: `str`<a id="task-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TaskExecuteRequest`](./induced_ai_python_sdk/type/task_execute_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TaskExecuteResponse`](./induced_ai_python_sdk/pydantic/task_execute_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/autonomous` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
