import json
from datetime import timedelta
from pathlib import Path
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Optional

from semgrep.rule import Rule


class PerfTracker:
    events: List[Dict[str, Any]] = []

    def record(self, time: timedelta, rule: Rule, file: Optional[Path] = None) -> None:
        self.events.append(
            dict(time=time.total_seconds(), rule=rule.id, file=str(file))
        )

    def dump(self, stream: IO) -> None:
        for event in self.events:
            json.dump(event, stream)
            print(file=stream, flush=True)
        self.events = []


Tracker = PerfTracker()
