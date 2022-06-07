# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2022 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the handler for the 'safe_deployment_abci' skill."""

from packages.valory.skills.abstract_round_abci.handlers import ABCIRoundHandler
from packages.valory.skills.abstract_round_abci.handlers import (
    ContractApiHandler as AbstractRoundContractApiHandler,
)
from packages.valory.skills.abstract_round_abci.handlers import (
    HttpHandler as AbstractRoundHttpHandler,
)
from packages.valory.skills.abstract_round_abci.handlers import (
    LedgerApiHandler as AbstractRoundLedgerApiHandler,
)
from packages.valory.skills.abstract_round_abci.handlers import (
    SigningHandler as AbstractRoundSigningHandler,
)


ABCIHandler = ABCIRoundHandler
HttpHandler = AbstractRoundHttpHandler
SigningHandler = AbstractRoundSigningHandler
LedgerApiHandler = AbstractRoundLedgerApiHandler
ContractApiHandler = AbstractRoundContractApiHandler